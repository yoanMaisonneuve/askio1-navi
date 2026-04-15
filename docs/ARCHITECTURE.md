# ARCHITECTURE · Mapping formel → technique

> Version : **v1.0** · 2026-04-15
> Source formelle : [`EQUATIONS.md`](./EQUATIONS.md) v1.0
> Cible : aski01.com + repo `askio1-navi` (NAVI v1.0)
> Phase 2 du pivot Blueprint (Phase 1 = catalogue, Phase 2 = mapping, Phase 3 = prototype)

Ce document traduit la théorie Blueprint (C0-C5) en **choix d'implémentation concrets**. Chaque opérateur formel (F, G, A, Π) reçoit un composant technique, un protocole I/O, un coût estimé et un état `implemented / partial / todo`.

---

## 0. Règles d'architecture

| # | Règle | Justification |
|---|---|---|
| A1 | **Tout composant référence un ID canonique** de `EQUATIONS.md` (ex: `BNGUR-ENGU-01`, `I17`) | I13 · interdiction de modifier un invariant sans justification |
| A2 | **Orchestrateur = source de vérité du state** ; MCP agents sont sans état | I19 · priorité du stable · évite divergence de state |
| A3 | **Un seul LLM frontier par tick** ; les MCP peuvent utiliser des modèles plus légers | Coût · latence · I20 priorité du simple |
| A4 | **Persistence append-only** pour events/décisions ; mutation uniquement sur la vue dérivée | GS11 réversibilité structurelle + I23 traçable |
| A5 | **PEC obligatoire** à chaque évolution de code (Extraction → Transformation → Validation) | Invariant PEC (C0.2) |
| A6 | **Observabilité = first class** : chaque appel F/G/Π/A logué avec latence + tokens + coût | I17 priorité du mesurable |
| A7 | **Langue par défaut API = français** ; multilingue = couche de traduction en amont | Identité Yoan + ICP |

---

## 1. Mapping opérateurs → composants

### Tableau maître

| Opérateur (C1) | Rôle théorique | Composant technique | Modèle/Stack | Statut |
|---|---|---|---|---|
| **F** | Lecture/interprétation d'état `F(x_t)` | `clarifier-mcp` (MCP agent) | Claude Haiku 4.5 + embeddings multilingues | 🔄 partial (code Python existant sans LLM) |
| **G** | Évolution interne `x_{t+1} = G(...)` | **Orchestrateur** (FastAPI service) | Python 3.12 · Pydantic v2 · Temporal.io (workflow) | ⬜ todo |
| **A** | Opérateur d'attraction vers A₀, A_profond | `attractor-service` (retrieval) | pgvector sur Supabase + k-NN cosine | ⬜ todo |
| **Π** | Politique d'action `Π = Π_dir + Π_corr + Π_sync` | `navigator-mcp` + `coordinator-mcp` | Claude Sonnet 4.6 (Π_dir) · rule engine (Π_corr) · pub/sub (Π_sync) | ⬜ todo |
| **δ_t** | Correction directionnelle `(dF_x)†(y-F(x))` | Module `drift-corrector` dans orchestrateur | Vector arithmétique sur embeddings | 🔄 partial |
| **C_corr(t)** | Correction de dérive | `navigator-mcp` · policy tree | Rule engine + LLM fallback | ⬜ todo |
| **C_sync(t)** | Synchronisation multi-pilotes | `sync-channel` (Supabase Realtime) | WebSocket + pub/sub | ⬜ todo |
| **ϟP(t)** | Équation de présence | `presence-meter` dans orchestrateur | Time series · Prometheus + calcul live | ⬜ todo |
| **C(t)** | Charge mentale | `load-meter` (idem) | Signal behavioral + proxy heuristiques | ⬜ todo |
| **τ** | Délai directionnel | `drift-detector` (polling sur events) | Fenêtre glissante · seuil configurable | ⬜ todo |
| **g\*** | But actif | Typed JSON schema · champ du State | Pydantic `Goal(description, embedding, horizon)` | ⬜ todo |
| **V** | Vision (attracteur lointain) | Enregistré par utilisateur lors de l'onboarding | Texte + embedding figé + révision trimestrielle | ⬜ todo |

### Désambiguïsation du symbole `A`

Résolution du gap identifié dans EQUATIONS.md (section Gaps) :

| Symbole | Sémantique | Implémentation |
|---|---|---|
| `A` (attracteur) | ensemble compact invariant, ex: A₀, A_profond | Row dans table `attractors` + embedding |
| `A(·)` (opérateur) | pull vers attracteur | Fonction `pull(state, attractor) → corrected_state` |
| `𝒜` (espace d'actions) | ensemble des actions candidates | Liste/générateur dans `navigator-mcp` |

---

## 2. Stack technique

### 2.1 Frontend (aski01.com)

| Couche | Choix | Motivation |
|---|---|---|
| Framework | **Next.js 15 (App Router)** | SSR + RSC · aligne avec C3 "corridor, pas menu" |
| Hébergement | **Vercel Edge** | Cold-start minimal · proximité CDN |
| UI | **shadcn/ui + Tailwind** | Discipline design + I21 lisibilité |
| Auth | **Supabase Auth** (email + OAuth) | Intégré au backend |
| State client | **Zustand** (léger) + **TanStack Query** | Évite Redux — I20 priorité du simple |
| Voice | **Web Speech API** + fallback Whisper.cpp | Yoan travaille voice-first (CONTEXT.md) |

### 2.2 Backend (orchestrateur + MCP)

| Service | Tech | Port | Rôle |
|---|---|---|---|
| `orchestrator` | FastAPI + Uvicorn | 8000 | Implémente G, le loop BNGUR-ENGU-01, routing PDD1-PDD7 |
| `clarifier-mcp` | MCP Python SDK | 9001 | F(x_t) — extraction intention structurée |
| `navigator-mcp` | MCP Python SDK | 9002 | Π_dir — sélection corridor |
| `stabilizer-mcp` | MCP Python SDK | 9003 | BNGUR-03/04 — ϟP, C(t), M_τ |
| `attractor-service` | FastAPI | 8001 | A(·) — retrieval attracteurs |
| `video-worker` | Celery + Redis | — | Pipeline vidéo (SkyReels/Open-Sora/LTX) async |
| `sync-channel` | Supabase Realtime | — | C_sync pub/sub |

### 2.3 Data layer

| Store | Tech | Contenu |
|---|---|---|
| Relationnel | **Supabase Postgres 16** | Users, sessions, goals, decisions, events |
| Vectoriel | **pgvector** (extension) | Embeddings : attracteurs, états, intentions, docs |
| Cache/Queue | **Redis** (Upstash) | Sessions chaudes · file Celery · rate limits |
| Object | **Supabase Storage** | Vidéos générées · audio · images utilisateur |
| Logs | **Logtail** (ou Supabase logs) | Traces append-only observabilité |

### 2.4 Modèles IA

| Usage | Modèle | Contexte | Coût approx. |
|---|---|---|---|
| F — interprétation légère | **Claude Haiku 4.5** | Chaque input utilisateur | $0.001 / appel |
| Π_dir — décision directionnelle | **Claude Sonnet 4.6** | 1-2× par tick | $0.01 / appel |
| Raisonnement complexe (fallback) | **Claude Opus 4.6** | Cas ambigus · rare | $0.05 / appel |
| Embeddings | **multilingual-e5-large** (self-hosted OVH) ou **voyage-multilingual-2** | Chaque message + docs | ~$0 self-host |
| Vidéo IA | SkyReels · Open-Sora · LTX | À la demande | OVH H100 spot |
| Reranking | **bge-reranker-v2-m3** (self-hosted) | Si > 50 candidats retrieval | ~$0 |

**Règle de sélection** (A3 + Reformulateur 6 couches) : micro-appel Haiku en amont pour choisir le modèle optimal selon qualité/dollar. Pipeline multi-agents ne consomme pas de tokens sur le routing.

---

## 3. Le loop BNGUR-ENGU-01 en code

**Équation :**
```
x_{t+1} = G(A(F(x_t) + (dF_{x_t})† (y - F(x_t)))) + C_corr(t) + C_sync(t)
```

### 3.1 Séquence d'exécution (un tick)

```
┌─────────────────────────────────────────────────────────────┐
│ Tick t — user input received                                │
└─────────────────────────────────────────────────────────────┘
          │
          ▼
[1] LOAD x_t from Supabase (session state)
          │
          ▼
[2] F(x_t) — clarifier-mcp
    • Haiku call : extract {intent, emotion, entities}
    • embed intent → e_t
    • write to events(type="F", payload=...)
          │
          ▼
[3] PDD1 — état stable ?
    ├── NON → T3 (stabilizer-mcp) → retry ou close
    └── OUI → continue
          │
          ▼
[4] PDD2 — intention claire ? (score LLM)
    ├── NON → T4 refroidissement · ask clarification
    └── OUI → continue
          │
          ▼
[5] PDD3 — charge sous limite ? (C(t) < L)
    ├── NON → T4 refroidissement
    └── OUI → continue
          │
          ▼
[6] PDD4 — dérive détectée ? (τ > seuil)
    ├── OUI → T2 correction (C_corr)
    └── NON → continue
          │
          ▼
[7] A(F(x_t) + δ_t) — attractor-service
    • pgvector k-NN : retrieve A₀, A_profond, closest corridors
    • δ_t = (dF_x)† (y - F(x_t))
    •   computed as : projection linéaire sur basis d'embeddings
    • return corrected_embedding c_t
          │
          ▼
[8] Π(o_t, x_t, C_t, g*) — navigator-mcp
    • Sonnet call : choisir a_t dans A
    • a_t = argmin_{a∈A} d(a(s_t, C_t), g*)
    •   d(·,·) = 1 - cosine_similarity (voir §5)
    • Π_dir = LLM decision
    • Π_corr = rule engine sur invariants I1-I28
    • Π_sync = publish event to sync-channel
          │
          ▼
[9] G — orchestrator commit
    • x_{t+1} = commit(c_t, a_t, C_corr, C_sync)
    • write to sessions + events (append-only)
    • ϟP(t+1) computed
          │
          ▼
[10] OUTPUT back to user (with I7 clarté, I9 explicite)
```

### 3.2 Contrats I/O (Pydantic)

```python
# navi/contracts.py
from pydantic import BaseModel, Field
from typing import Literal

class State(BaseModel):
    """x_t — état directionnel au temps t"""
    session_id: str
    tick: int
    s_dir: list[float]   # S_dir · embedding directionnel (dim=1024)
    s_mem: dict          # S_mem · contexte mémoriel récent
    s_err: list[float]   # S_err · correction d'erreur accumulée
    C_t: float           # charge mentale courante
    goal_active: "Goal | None"
    attractor_default: str  # A₀ id

class Goal(BaseModel):
    """g* — but actif"""
    id: str
    description: str
    embedding: list[float]
    horizon: Literal["action", "but", "vision"]  # T_A << T_G << T_V
    lambda_: float = 0.5  # pondération distance→vision

class Intent(BaseModel):
    """F(x_t) output"""
    raw_text: str
    embedding: list[float]
    entities: list[str]
    emotion: str
    confidence: float

class Action(BaseModel):
    """a_t — action choisie"""
    id: str
    type: Literal["clarify", "stabilize", "navigate", "close", "integrate", "redirect", "converge"]
    payload: dict
    invariants_check: dict[str, bool]  # I_i(a) pour i ∈ {1..28}
```

---

## 4. Les 10 rôles → MCP agents

Implémentation progressive. V1.0 cible les 4 premiers ; V2 complète jusqu'à 10.

| Rôle (C4.3) | MCP agent | Priorité | Version |
|---|---|---|---|
| 1 · Leader-Orchestrateur | **`orchestrator-core`** (= pas un MCP, c'est le core) | P0 | V1.0 |
| 2 · Gestionnaire de Projet | `planner-mcp` | P1 | V1.0 |
| 3 · Créateur-Collecteur | `collector-mcp` | P2 | V1.1 |
| 4 · Coach-Spécialiste | `coach-mcp` | P2 | V1.1 |
| 5 · Bibliothécaire-Archiviste | `archivist-mcp` | P0 (I6 archivage obligatoire) | V1.0 |
| 6 · Médiateur | `mediator-mcp` | P1 | V1.1 |
| 7 · Designer Senior | `designer-mcp` | P3 | V2.0 |
| 8 · Développeur Senior | `dev-mcp` | P3 | V2.0 |
| 9 · Visionnaire | `visionary-mcp` | P2 | V1.1 |
| 10 · Directeur des Ventes | `market-mcp` | P3 | V2.0 |

**V1.0 minimum** (Phase 3 prototype) :
- `orchestrator-core` (implémente G)
- `clarifier-mcp` (implémente F)
- `navigator-mcp` (implémente Π_dir)
- `archivist-mcp` (implémente I6, traçabilité)

Pipeline fermé simplifié en V1.0 :
```
user → clarifier → navigator → archivist → user
                       ↑           │
                       └───────────┘ (feedback loop)
```

---

## 5. Décisions formelles (résolution des gaps EQUATIONS.md)

### 5.1 Distance directionnelle `d(·, ·)`

**Décision** : `d(u, v) = 1 - cos(u, v)` sur embeddings normalisés (L2).

**Justification** :
- Pseudo-métrique (pas une vraie métrique car triangle faible), suffisant pour argmin
- Implémentable en pgvector (opérateur `<=>`)
- Comparable cross-domain (texte, image embeddings multimodaux)
- Stable sous perturbation `ε(t)` (cf dynamique convergence C3.7)

**Alternative considérée** : Wasserstein-1 sur distributions d'actions — trop coûteux pour V1.0, réservé V2.0.

### 5.2 Paramètres `α, λ, k`

| Paramètre | Rôle | Valeur initiale | Protocole de calibration |
|---|---|---|---|
| **α** (décroissance charge) | `e^{-αC(t)}` dans ϟP | `0.5` | Fit par utilisateur après 30 sessions · MLE sur feedback engagement |
| **λ** (pondération vision) | `d(s,g) + λ·d(g,V)` | `0.3` | A/B test V1.0 vs V1.1 sur rétention 7j |
| **k** (refroidissement ENCM-1) | `Rb·Rs ≥ k·(Cs·Ct)` | `1.2` | Constante hard-coded V1.0 · ajustable V2.0 |

**Règle** : paramètres stockés dans `config/blueprint.toml`, surchargeables par user-overrides en table `user_preferences`. I17 priorité du mesurable → logging systématique pour enrichir calibration.

### 5.3 Invariants manquants I5, I27

**Proposition de comblement** (à valider Yoan) :
- **I5 · Priorité du rituel** : Toute boucle majeure doit être encadrée par un rituel d'ouverture et de fermeture. (Dérive de BNGUR-06)
- **I27 · Interdiction de la surcharge relationnelle** : Aucune action ne peut être prise si la charge relationnelle (H proxy) chute sous un seuil critique. (Dérive de C3.6)

**Alternative** : retirer I5/I27 et renuméroter → passer à **26 invariants**. Plus propre mais casse la FORMULE 29 (29 = 28 + non-comparatif). **Mon reco : combler avec les propositions ci-dessus**. À trancher.

### 5.4 `(dF_x)†` — pseudo-inverse

**Décision V1.0** : approximation linéaire locale par **projection Moore-Penrose discrète** :
```python
def pseudo_inverse_step(F_x_t, y, alpha=0.1):
    """δ_t ≈ α · (y - F(x_t))  — descente simple sur embedding"""
    return alpha * (y - F_x_t)
```
**V2.0** : autograd via PyTorch si F devient un modèle fine-tuné différentiable.

---

## 6. Site aski01.com — parcours utilisateur

Traduction C3 "corridor, pas menu" en UX concrète.

### 6.1 Onboarding (activation V, A₀)

1. **Landing** — un seul CTA, pas de menu (C3.10 PNC-01 : Reconnaître)
2. **Capture V (vision)** — 3 questions voice/texte → embedding figé
3. **Capture A₀ (attracteur défaut)** — journal 3 jours · extraction automatique `argmax T(A)`
4. **Premier tick BNGUR-ENGU-01** — user pose une intention → pipeline F→A→Π→G en <2s

### 6.2 Session régulière

- **Corridor unique** affiché : `g*` + prochaine action `a_t`
- **Jauges** : ϟP (présence) · C(t) (charge) · τ (dérive)
- **Fermetures rituelles** (BNGUR-06) : quotidienne · hebdo · trimestrielle
- **Override explicite** requis pour changer de branche (I8 interdiction dérive thématique)

### 6.3 Pricing — aligné A₀ économique (C0.2)

**"L'argent est la clé directionnelle"** → pas de free tier permanent. Gratuit 14 jours (onboarding complet), puis :

| Plan | Prix | Qui |
|---|---|---|
| **Pilote** | 19 CAD/mois | Usage individuel · toutes boucles · 500 ticks/mois |
| **Capitaine** | 49 CAD/mois | Usage intensif · vidéo IA · ticks illimités · sync collectif |
| **Équipage** | 199 CAD/mois | Jusqu'à 10 utilisateurs · C_sync multi-pilotes (BNGUR-07) |

**Stack paiement** : Stripe (via Supabase extension) · abonnements mensuels auto-renouvelables · facturation à l'usage pour vidéo.

---

## 7. Sécurité · Observabilité · Conformité

### 7.1 Sécurité

| Couche | Mesure |
|---|---|
| Auth | Supabase Auth · MFA obligatoire Équipage+ |
| Secrets | `.env` jamais commit · Vercel env vars · Supabase Vault |
| API | Rate-limit 60 req/min/user · WAF Cloudflare |
| Data | Chiffrement at-rest (Supabase) + in-transit (TLS 1.3) |
| Prompts | Sanitization input · jamais d'exécution code utilisateur |
| PII | Minimisation · droit effacement GDPR · logs 90 jours max |

### 7.2 Observabilité

Chaque opérateur logue : `{op, tick, session, latency_ms, tokens_in, tokens_out, cost_usd, status}`.

**Métriques clés** :
- Latence p95 par opérateur (objectif F < 500ms, Π < 2000ms)
- Coût par tick (objectif < $0.02 V1.0, < $0.005 V2.0 avec cache)
- Taux de dérive détectée (τ > seuil)
- Rétention 7j / 30j (corrélée à ϟP moyen)

**Stack** : OpenTelemetry → Logtail + Grafana OSS self-hosted (OVH BHS, cohérent avec GPU-infra).

### 7.3 GE-HALLU-01

Protocole anti-hallucination (C0.2) → implémenté :
- Toute réponse LLM passe par **validator** qui vérifie citations vs retrieval
- Si < 70% coverage → étiquette `[incertain]` explicite dans l'output (I9 interdiction de l'implicite)
- Log spécial `hallucination_risk=true` → feed du fine-tune futur

---

## 8. Repos & déploiement

### 8.1 Répartition des repos

| Repo | Visibilité | Rôle |
|---|---|---|
| `askio1-navi` | public | Code NAVI (open source) · librairie directionnelle |
| `askio1-site` | privé (à créer) | Next.js · aski01.com · UI + auth |
| `askio1-orchestrator` | privé (à créer) | FastAPI · G · BNGUR loop |
| `askio1-mcp` | public · monorepo | Les MCP agents (1 package par agent) |
| `Blueprint-memory` | privé | Mémoire partagée Yoan × Claude (ici) |
| `Enter-Game` | public | Protocole d'efficacité solo-founder |

### 8.2 Infra

Aligné sur décisions verrouillées (CONTEXT.md) :

| Cible | Infra | Détail |
|---|---|---|
| Frontend | Vercel Edge | Next.js |
| Backend | OVH BHS (ca-east) · Kubernetes MKS | FastAPI + MCP servers · Docker |
| GPU training | OVH H100 · spin up/down | Budget 20 CAD/session max (I2 limite charge) |
| GPU inference vidéo | Vast.ai spot RTX 4090 (CA only) | Fallback OVH si Vast saturé |
| DB | Supabase managed | Postgres + pgvector + Realtime + Auth + Storage |
| Cache/Queue | Upstash Redis | Serverless · pay per request |

---

## 9. Roadmap d'implémentation

### V1.0 — Prototype (Phase 3) · cible 4 semaines

- [ ] `orchestrator-core` · FastAPI scaffold · state machine BNGUR-ENGU-01
- [ ] `clarifier-mcp` · Haiku wrapper · returns `Intent`
- [ ] `navigator-mcp` · Sonnet wrapper · returns `Action`
- [ ] `archivist-mcp` · append-only event log
- [ ] Supabase schema · `sessions`, `events`, `attractors`, `goals`, `users`
- [ ] pgvector index sur `attractors.embedding`
- [ ] 1 end-to-end test : user input → clarifier → navigator → archivist → response
- [ ] Budget prototype ≤ 50 CAD (20 OVH + 30 Claude API test)

### V1.1 — Extension · 4-8 semaines

- [ ] `stabilizer-mcp` + ϟP/C(t) meters
- [ ] `planner-mcp` + `mediator-mcp` + `visionary-mcp`
- [ ] Onboarding complet (capture V, A₀)
- [ ] UI aski01.com minimal (Next.js)
- [ ] Stripe intégration pricing Pilote
- [ ] Observabilité Grafana + Logtail

### V2.0 — Plateforme · 2-4 mois

- [ ] Les 10 rôles déployés
- [ ] Collectif BNGUR-07 (sync multi-pilotes · WebSocket)
- [ ] Vidéo IA pipeline intégré
- [ ] Scaling international (EN · FR · DE · BR)
- [ ] Fine-tune custom sur dataset propre (Wan2.1 · CogVideoX)

---

## 10. Risques & mitigations

| Risque | Impact | Probabilité | Mitigation |
|---|---|---|---|
| Coût Claude API dérape | Élevé | Moyen | Cache agressif · Haiku par défaut · budget alert 18 CAD (I2) |
| Latence > 3s par tick | Élevé (UX) | Moyen | Parallélisme F/A · streaming · fallback local embedding |
| Hallucination mesure ϟP/C(t) | Élevé (crédibilité) | Élevé | Proxies behavioral robustes · opt-in self-report · GE-HALLU |
| pgvector ne scale pas (>1M vecs) | Moyen | Faible V1 | Migration vers Pinecone/Weaviate V2 si besoin |
| Perte de state orchestrateur | Critique | Faible | Temporal.io durable execution · replay events |
| Vendor lock Anthropic | Moyen | Moyen | Abstraction LLM provider · fallback OpenAI/Mistral |
| Utilisateur ne "sent" pas la directionnalité | Critique (thèse) | ? | Onboarding scientifique C3 · mesure ϟP early · iterate |

---

## 11. Tests & critères d'acceptation V1.0

### Tests techniques (I14 test obligatoire)
- [ ] Tick end-to-end < 3s p95
- [ ] F, Π, G tous logués avec trace ID
- [ ] Invariants I1-I28 vérifiés par `invariants_check` sur chaque `Action`
- [ ] Rollback fonctionnel sur erreur (PEC §6)

### Tests produit (I18 reproductible)
- [ ] 3 utilisateurs pilotes · onboarding sans assistance
- [ ] ϟP mesuré pré/post-session sur 20 sessions
- [ ] τ détection fonctionne (alerte quand user dérive)
- [ ] Rétention J7 ≥ 40% (benchmark loose)

### Tests fondamentaux (I15 vision en couches)
- [ ] Chaque commit mappe à un ID canonique `EQUATIONS.md`
- [ ] Aucun composant ne contredit I1 (priorité du réel)
- [ ] Documentation à jour (I21 lisible · I22 navigable)

---

## Historique

- **v1.0** · 2026-04-15 · Mapping initial opérateurs formels → stack technique. Stack : Next.js + Supabase + FastAPI + MCP + Claude (Haiku/Sonnet/Opus). Résolution des 4 gaps EQUATIONS.md (d(·,·) = 1-cos, α/λ/k initiaux, I5/I27 comblés proposition, (dF_x)† Moore-Penrose discret). Roadmap V1.0 → V2.0.

---

*Prochaine action* : **Phase 3** — scaffold `askio1-orchestrator` (FastAPI) + 2 MCP agents (`clarifier-mcp`, `navigator-mcp`) avec un test end-to-end exécutable. Budget cible : 50 CAD, 4 semaines. Prompt : `go phase 3`.
