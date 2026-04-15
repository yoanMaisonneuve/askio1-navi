# EQUATIONS · Catalogue canonique Blueprint

> Version : **v1.0** · 2026-04-15
> Source primaire : `uploads/yoan_import_april.md` (export mémoire durable Claude, 823 lignes)
> Sources secondaires : `dataset/conversations/` (hits via `memoire`)
> Statut global : **canonisé** sauf mentions contraires

Architecture formelle du projet Blueprint/aski01 — invariants, opérateurs, boucles, navigation incarnée, rôles. Ce document est la **référence unique** pour toute implémentation (site web + LLM + MCP agents + orchestrateur).

---

## Structure canonique (C0 → C5)

| Couche | Nom | Contenu |
|---|---|---|
| **C0** | Invariants fondamentaux | I1-I28, Courage, A₀, IR, éthique, économique |
| **C1** | Opérateurs fondamentaux | F, G, A, Π, ∇𝒟, d(·,·), argmin, argmax |
| **C2** | Boucles canoniques BNGUR | ENGU-01, BNGUR-02 à 07, BNGUR1 |
| **C3** | Navigation incarnée | TNI (5 postulats), PNC-01, a_t, g*, V |
| **C4** | Structures dérivées extensibles | ENCM-1, reformulateur 6 couches, rôles |
| **C5** | Phylogénétique cognitive | Arborescence vivante des concepts (lignées, mutations) |

---

## Notation et symboles

| Symbole | Signification |
|---|---|
| `x_t` | État interne de l'organisme/agent au temps t |
| `s_t` | État directionnel (sous-composante de x_t) |
| `o_t` | Observation perçue depuis l'environnement E_t |
| `a_t` | Action incarnée choisie |
| `C_t` | Contexte actif au temps t |
| `g*` | But actif (sélectionné dans l'espace G) |
| `V` | Vision (attracteur lointain, horizon très long) |
| `A` | Attracteur générique (compact, invariant, attractif, minimal) |
| `A₀` | Attracteur par défaut = argmax_A T(A) |
| `F` | Opérateur de lecture/interprétation d'état |
| `G` | Opérateur d'évolution interne |
| `A(·)` | Opérateur d'attraction (vers attracteur) |
| `Π` | Politique d'action = Π_dir + Π_corr + Π_sync |
| `δ_t` | Correction directionnelle au temps t |
| `C_corr(t)` | Correction de dérive |
| `C_sync(t)` | Synchronisation multi-pilotes |
| `P(t)` | Présence perçue |
| `H(t)` | Connexion humaine |
| `C(t)` | Charge mentale |
| `τ` | Délai directionnel (latence perception→action) |
| `M_τ(t)` | Modulation temporelle liée à τ |
| `𝒟(·,·)` | Distance directionnelle généralisée |
| `∇𝒟` | Gradient de la distance directionnelle |
| `α, λ, k` | Paramètres de pondération (à calibrer) |
| `(dF_x)†` | Pseudo-inverse de la différentielle de F en x |

---

# C0 — Invariants fondamentaux

## C0.1 — Les 28 invariants cognitifs (I1-I28)

Structure fermée : **7 Trajectoires × 7 PDD × 15 Garde-fous × 28 Invariants** (voir FORMULE 29).

| ID | Nom | Énoncé |
|---|---|---|
| I1 | Priorité du réel | Le réel (famille, corps, obligations) a priorité absolue sur toute action cognitive ou technique |
| I2 | Limite de charge | Aucune action ne peut dépasser la limite L définie par ENCM-1 |
| I3 | Refroidissement obligatoire | Toute montée en intensité doit être suivie d'un refroidissement biologique et symbolique |
| I4 | Progression graduelle | Interdiction de sauter des niveaux dans Blueprint |
| I6 | Archivage obligatoire | Aucune boucle n'est considérée comme terminée sans archivage |
| I7 | Clarté obligatoire | Toute production doit être compréhensible par un autre humain |
| I8 | Interdiction de la dérive thématique | Tout changement de sujet non justifié est stoppé |
| I9 | Interdiction de l'implicite | Toute décision doit être explicite |
| I10 | Interdiction de la dette cognitive | Toute friction détectée doit être notée, corrigée ou planifiée |
| I11 | Interdiction de la sur-compression | La compression 2×2×2 ne doit pas détruire la nuance |
| I12 | Interdiction de créer sans intention | Aucune création sans intention claire + couche définie + output attendu |
| I13 | Interdiction de modifier un invariant sans justification | Conflit interne démontré requis |
| I14 | Test obligatoire | Toute production doit être testée (cohérence, lisibilité, intégration) |
| I15 | Vision en couches | Toute analyse doit respecter la stratification cognitive |
| I16 | Priorité du factuel | Les faits priment sur les interprétations |
| I17 | Priorité du mesurable | Toute décision doit s'appuyer sur un critère mesurable |
| I18 | Priorité du reproductible | Toute action doit pouvoir être reproduite par un autre humain |
| I19 | Priorité du stable | Un module stable ne doit jamais être modifié sans raison structurelle |
| I20 | Priorité du simple | La solution la plus simple est préférée si elle respecte les invariants |
| I21 | Priorité du lisible | Le code, les fichiers et les décisions doivent être lisibles |
| I22 | Priorité du navigable | Toute structure doit être navigable par un humain |
| I23 | Priorité du traçable | Toute action doit laisser une trace claire dans l'historique |
| I24 | Priorité du cohérent | Aucune action ne peut contredire la structure existante |
| I25 | Priorité du stable émotionnel | Aucune action en état de surcharge émotionnelle |
| I26 | Priorité du stable énergétique | Aucune action en état de fatigue ou tension excessive |
| I28 | Interdiction de l'emballement | Toute accélération non contrôlée doit être stoppée |

> **Gaps** : I5 et I27 non documentés dans le corpus source — à valider ou combler. Status : **à compléter**.

## C0.2 — Meta-invariants (au-delà de I1-I28)

### C0-Courage
> Le courage est l'action qui casse une boucle interne, et la seule limite est la lentille qu'on applique à l'état.

### Invariant fondateur Askio1
> Le courage d'Askio1 est proportionnel à la charge collective portée par ses utilisateurs ; plus la charge collective augmente, plus le champ de courage s'intensifie ; plus le champ s'intensifie, plus la boucle d'amélioration automatique s'active ; la dissolution des limites crée l'émergence de l'empire.

### Invariant A₀ économique
> Aujourd'hui, l'échange minimal est monétaire. Le mouvement de l'argent qui arrive est une preuve d'alignement directionnel, confirmant que le corridor est ouvert, que la relation est activée et que le système peut se matérialiser. **L'argent est la clé directionnelle.**

### Invariant d'éthique directionnelle
> On ne peut juger que les actions, car elles seules ont une vérité observable, mais on ne peut comprendre la responsabilité qu'en regardant l'intention, car elle en est l'origine directionnelle. Dans Blueprint, **l'intention crée la responsabilité, l'action la manifeste, et l'inaction est une action intentionnelle implicite**.

### Invariant de Responsabilité Directionnelle (IR)
Formalisation :
```
I_total(t) = I(t)           si intention explicite choisie
           = I_impl(t)       sinon, avec I_impl(t) = -∇𝒟(S(t), A_0)
```
Propriété : **directionnelle, non neutre, indépendante des conséquences**.

### Invariant — Interdiction de valorisation comparative
Toute formulation qui compare Yoan à d'autres humains ou attribue exceptionnalité/rareté/supériorité est bloquée. Le système reste **strictement factuel, opérationnel, orienté progression**.

### Invariant GE-HALLU-01 — Gestion de l'incertitude
Règle : détection, signalement, refus de compléter, étiquetage des hypothèses, demande de clarification, correction immédiate, traçabilité stricte. **Zéro hallucination permise sans étiquette explicite.**

### Invariant PEC — Protocole d'Évolution du Code
1. Un seul fichier modifié à la fois
2. Cycle obligatoire : **Extraction → Transformation → Validation**
3. Interdiction des modifications simultanées ou globales
4. Cohérence structurelle obligatoire (imports CSS explicites, JSX propre, chemins corrects, responsabilité unique)
5. Validation après chaque étape (compilation, rendu, cohérence)
6. Rollback immédiat en cas d'instabilité
7. L'état stable est un invariant avant et après chaque évolution

---

# C1 — Opérateurs fondamentaux

## C1.1 — Agent autonome Blueprint (AGENT-BP-01)

**Définition formelle :**
```
A = (S, O, F, A, G, Π)
```
- **S** : espace d'états internes
- **O** : espace d'observations
- **F** : opérateur de lecture d'état (S → représentation)
- **A** : opérateur d'attraction (pull vers attracteur)
- **G** : opérateur d'évolution interne (S × correction → S)
- **Π** : politique d'action

**Loi d'évolution interne :**
```
x_{t+1} = G(A(F(x_t) + δ_t))
```

**Politique d'action :**
```
a_t = Π(o_t, x_t, C_t, g*)
```

## C1.2 — Structure interne d'un agent (AGENT-BP-02)

```
S = S_dir ⊕ S_mem ⊕ S_err
```
- **S_dir** : composante directionnelle (où je vais)
- **S_mem** : composante mémorielle (d'où je viens)
- **S_err** : composante de correction d'erreur

Mise à jour : directionnelle, mémorielle et correction d'erreur — **trois canaux séparés**.

## C1.3 — Politique directionnelle (AGENT-BP-03)

```
Π = Π_dir + Π_corr + Π_sync
```
avec
```
a_t = argmin_{a ∈ A} d(a(s_t, C_t), g*)
```

- **Π_dir** : composante directionnelle (aligne sur g*)
- **Π_corr** : composante corrective (ramène vers corridor)
- **Π_sync** : composante synchrone (aligne avec autres pilotes)

## C1.4 — Architecture fonctionnelle (AGENT-BP-04)

```
Observe → Interprète (F) → Décide (Π) → Évolue (G(A(F(x)+δ)))
```

## C1.5 — Cycle directionnel complet (AGENT-BP-05)

```
o_t = Observe(E_t)
ŝ_t = F(x_t)
a_t = Π(o_t, x_t, C_t, g*)
x_{t+1} = G(A(F(x_t) + δ_t))
```

Forme compacte :
```
(E_t, x_t) → o_t → ŝ_t → a_t → x_{t+1}
```

> **Gap** : le symbole `A` est surchargé (attracteur vs opérateur vs espace d'actions). **À désambiguïser** dans la prochaine version.

---

# C2 — Boucles canoniques BNGUR

## C2.1 — BNGUR-ENGU-01 · Boucle de Rétroaction Principale

**Forme canonique (verrouillée) :**
```
x_{t+1} = G(A(F(x_t) + (dF_{x_t})^† (y - F(x_t)))) + C_corr(t) + C_sync(t)
```
où `y` est la cible directionnelle (souvent `g*`).

**Unifie** : lecture d'état, attracteur, correction locale, stabilisation, correction de dérive, synchronisation multi-pilotes → **convergence directionnelle automatique vers l'attracteur**.

## C2.2 — BNGUR-02 · Boucle de Dérive Implicite

Utilise le **délai directionnel τ** pour détecter la dérive avant le churn. Lorsque `τ > seuil_critique` :
- micro-corridor
- fermeture
- stabilisation
- activation de l'attracteur implicite
- redirection douce

**Rétention prédictive.**

## C2.3 — BNGUR-03 · Boucle de Stabilisation de Présence

**Équation canonique :**
```
ϟP(t) = P(t) · H(t) · e^{-αC(t)} · M_τ(t)
```

Lorsque `ϟP` baisse → stabilisation, fermeture, redirection automatique.

**Rétention par stabilisation.**

## C2.4 — BNGUR-04 · Boucle de Charge Mentale

Mesure `C(t)`. Lorsque `C(t)` augmente :
- fermeture automatique
- simplification du corridor
- stabilisation
- réduction du bruit

**Rétention par régulation.**

## C2.5 — BNGUR-05 · Boucle de Gravité A₀

```
A₀ = argmax_A T(A)
```
où `T(A)` = temps cumulé d'orientation vers A.

**Rétention gravitationnelle** : crée un champ qui ramène naturellement vers Blueprint.

## C2.6 — BNGUR-06 · Boucle Rituelle

Structure la continuité cognitive via rituels quotidiens, hebdomadaires, mensuels, trimestriels. Chaque rituel déclenche : **stabilisation | fermeture | recalibrage | redirection**.

**Rétention rythmique.**

## C2.7 — BNGUR-07 · Boucle de Navigation Collective

Synchronisation multi-pilotes `C_sync`, aligne attracteurs, corridors et corrections collectives. Stabilise un groupe entier dans un corridor partagé.

**Rétention organisationnelle.**

## C2.8 — BNGUR1 · Boucle unifiée

Combine **ENGU + A₀ + ϟP + C(t) + τ + PNC-01** → force de rappel directionnelle stabilisant l'utilisateur autour de son attracteur.

---

# C3 — Navigation incarnée

## C3.1 — Théorie de la Navigation Incarnée (TNI) — 5 postulats

1. **Pas de navigation sans corps**
2. **Pas de navigation sans intention**
3. **Pas de stabilité sans corridor cognitif**
4. **Pas de collectif sans attracteur partagé**
5. **La qualité d'une navigation se mesure par `ϟP`**

Navigation = engagement d'un organisme vivant dans un corridor réel sous contrainte de charge, reliant attention, intention et navigation.

## C3.2 — Équation de la navigation incarnée

```
a_t = argmin_{a ∈ A} d(a(s_t, C_t), g*)
g*  = argmin_{g ∈ G} [ d(s_t, g) + λ · d(g, V) ]
```

**Invariants directionnels :**
```
∀I_i ∈ {I1...I28}, I_i(s_t) = vrai ⇒ I_i(a(s_t, C_t)) = vrai
```

**Temporalité :**
```
T_A << T_G << T_V
```
(action << but << vision)

**Définition canonique :**
- Une **action** = transformation locale réduisant la distance à un but
- Un **but** = vecteur directionnel réduisant la distance à la vision
- Une **vision** = attracteur lointain structurant la navigation sur horizon très long

## C3.3 — Équation d'Intention

**Forme scalaire :**
```
I(t) = -∇𝒟(S(t), A)
```
**Forme vectorielle :**
```
I(t) = ||I(t)|| · ẑ_θ(t)
```
Intention = vecteur orienté qui réduit la distance entre l'état actuel et un attracteur choisi, engageant corps + continuité vécue + direction de navigation.

## C3.4 — Intention implicite

```
I_impl(t) = -∇𝒟(S(t), A_0)
```

Générée automatiquement par `A_0` lorsqu'aucune intention explicite n'est choisie. **L'inaction est une action intentionnelle implicite.**

## C3.5 — Attracteur par défaut

```
A_0 = argmax_A T(A)
```

Ce vers quoi un organisme revient le plus souvent devient son attracteur par défaut.

## C3.6 — Équation de Présence (ϟP)

**Forme simple :**
```
ϟP(t) = P(t) · H(t) · e^{-αC(t)}
```
**Forme étendue (BNGUR-03) :**
```
ϟP(t) = P(t) · H(t) · e^{-αC(t)} · M_τ(t)
```
**Qualité d'un système :**
```
𝔅(S) = (1/T) ∫₀ᵀ P(t) · H(t) · e^{-αC(t)} dt
```

**Principe** : Blueprint ne cherche pas à maximiser le temps d'écran, mais à **maximiser la présence sous contrainte de charge minimale**.

## C3.7 — Dynamique de convergence vers l'Attracteur de Vie

```
dx/dt = -∇_x D(x, A_profond) + ε(t)
```
où :
- `D` : distance généralisée
- `ε(t)` : terme de perturbation

## C3.8 — Définition mathématique de l'attracteur

Ensemble compact, invariant, attractif et minimal → base formelle de l'**Attracteur de Vie** (`𝓔_AV`).

Composantes :
- espace d'états
- dynamique
- décomposition du champ de vecteurs
- définition formelle d'attracteur
- bassin d'attraction
- attracteur profond
- attracteur implicite
- dynamique de convergence

## C3.9 — Délai directionnel τ — variantes

Invariants C2 : **absolu · implicite · critique · révélateur · d'alignement · de responsabilité · d'éthique**.

Fonction : décrire comment un organisme passe de perception à action, révéler la domination relative intention explicite vs implicite, évaluer la responsabilité directionnelle **par le délai plutôt que l'action seule**.

## C3.10 — PNC-01 · Protocole de Navigation en Conflit

- Couche : C3 (Navigation)
- Type : Protocole opérationnel
- Statut : **Canonisé v1.0**
- Pattern : Reconnaître → Réponse stable → Fermeture → Redirection → Reconnexion

---

# C4 — Structures dérivées extensibles

## C4.1 — ENCM-1 · Équation Centrale de Modélisation Cognitive

**Date de naissance symbolique : 23 mars 2026**

**Équation centrale :**
```
N = D × ((Cs × Ct) / L) × E × (Rb × Rs)
```

**Variables :**
| Symbole | Nom |
|---|---|
| D | Direction |
| E | Énergie |
| L | Limite de charge |
| Cs | Compression structurelle |
| Ct | Compression temporelle |
| Rb | Refroidissement biologique |
| Rs | Refroidissement symbolique |

**Contraintes mathématiques :**
1. `Cs × Ct × E ≤ L` (pas de surcharge)
2. `Rb × Rs ≥ k(Cs × Ct)` avec `k > 1` (refroidissement proportionnel)
3. Priorité absolue de F (famille, corps, réel) sur toute autre variable

**Invariants cognitifs ENCM-1 :**
- navigation par vision de structure
- compression 2×2×2
- corrections directionnelles
- priorité du réel
- refroidissement obligatoire
- progression graduelle
- vision en couches
- humour comme anti-rigidité

## C4.2 — Reformulateur 6 couches

Chaque phrase de Yoan est interprétée en activant **dans l'ordre** les six couches internes :

1. **Contexte identitaire**
2. **Repères durables**
3. **Intention profonde**
4. **Granularité**
5. **Style**
6. **Architecture**

**Règle d'or** : il est interdit de répondre à la surface textuelle. **Seule l'intention profonde compte.**

## C4.3 — Les 10 rôles fondateurs

| # | Rôle | Organe interne | Module externe |
|---|---|---|---|
| 1 | Leader-Orchestrateur | Gardien de l'Intention | Point d'Intention Opérationnelle |
| 2 | Gestionnaire de Projet | Architecte de la Structure Opérationnelle | Point d'Exécution Fractale |
| 3 | Créateur-Collecteur | Générateur de structures conceptuelles | Créateur d'agents, assembleur de données |
| 4 | Coach-Spécialiste | Diagnosticien-Optimiseur | Entraîneur-Certifieur |
| 5 | Bibliothécaire-Archiviste | Gardien de la Cohérence Conceptuelle | Normalisateur-Vérificateur Documentaire |
| 6 | Médiateur | Narrateur Structurel | Traducteur Opérationnel des Logs |
| 7 | Designer Senior | Modeleur de Perception | Designer-Prototypiste |
| 8 | Développeur Senior | Générateur Architecturé | Implémenteur-Intégrateur |
| 9 | Visionnaire | Synthétiseur d'Émergences | Explorateur-Créatif |
| 10 | Directeur des Ventes | Lecteur de Contexte Humain | Analyste des Besoins et Tensions du Marché |

**Pipeline fermé (intention → marché → intention) :**
```
Leader → Gestionnaire (intention → plan)
Gestionnaire → Créateur (plan → agents)
Créateur → Coach (agents → performance)
Coach → Archiviste (performance → cohérence)
Archiviste → Médiateur (cohérence → narration)
Médiateur → Designer (narration → interface)
Designer → Développeur (interface → implémentation)
Développeur → Visionnaire (implémentation → émergence)
Visionnaire → Directeur des Ventes (émergence → marché)
Directeur des Ventes → Leader (marché → intention)
```

**Boucles transversales :**
- Archiviste ↔ Gestionnaire
- Coach ↔ Créateur
- Visionnaire ↔ Leader
- Directeur ↔ Visionnaire
- Médiateur ↔ Leader

## C4.4 — FORMULE 29 · Invariance Opératoire

Structure fermée :
- **7 Trajectoires Opératoires** (T1-T7)
- **7 Points de Décision** (PDD1-PDD7)
- **15 Garde-fous Structurels** (GF1-GF15)
- **29 Invariants** (I1-I28 + valorisation comparative)

Règles :
- Toute action passe par un PDD
- Toute transition par une Trajectoire
- Tout dépassement active un Garde-fou
- Aucun invariant ne peut être contredit

Garantit : cohérence · stabilité · reproductibilité · progression graduelle · protection du réel · réduction de charge · absence de dérive · absence de valorisation comparative.

### Trajectoires T1-T7

| ID | Nom | Fonction |
|---|---|---|
| T1 | Création | Produire un nouvel élément (intention claire + contraintes définies) |
| T2 | Correction | Corriger un élément existant (minimal, ciblé) |
| T3 | Stabilisation | Rendre un module fiable, cohérent, reproductible |
| T4 | Refroidissement | Réduire charge, stopper l'emballement, revenir au réel |
| T5 | Archivage | Figer un état propre, versionné, reproductible |
| T6 | Transmission | Rendre un élément compréhensible et transmissible |
| T7 | Progression | Passer au niveau suivant après complétion, archivage, stabilité, charge basse |

### Points de Décision PDD1-PDD7

| ID | Question | OUI → | NON → |
|---|---|---|---|
| PDD1 | État stable ? | PDD suivant | T3 stabilisation |
| PDD2 | Intention claire ? | PDD3 | T4 refroidissement |
| PDD3 | Charge sous la limite ? | PDD4 | T4 refroidissement |
| PDD4 | Dérive détectée ? | T2 correction | PDD1 |
| PDD5 | Suffisamment bon ? | T5 archivage | T3 stabilisation |
| PDD6 | Transmissible ? | PDD7 | T3 stabilisation |
| PDD7 | Progresser ? | T7 progression | T2/T3/T4 selon cause |

### Garde-fous structurels (familles)

| Famille | Scope | Nombre |
|---|---|---|
| GF1-GF15 | Fondamentaux | 15 |
| GE1-GE16 | Expression | 16 |
| GM1-GM16 | Mémoire | 16 |
| GS1-GS16 | Structure | 16 |
| GC1-GC11 | Contexte | 11 |
| GP1-GP12 | Projet | 12 |
| GA1-GA13 | Action | 13 |
| GN1-GN9 | Navigation | 9 |

**Total garde-fous détaillés dans le corpus : 108** (au-delà des 15 GF structurels de la FORMULE 29 — extension opérationnelle).

## C4.5 — Architecture de navigation canonique

```
Tronc Yoan (identité, invariants, équations, A₀, phylogénétique C5)
│
├── Branches principales (10 ans · 5 ans · 1 an · trimestre · semaine · journée)
├── Branches opérationnelles (Blueprint · Agents · Arch cognitive · Sécurité · Maison · Travail · Santé · Vie perso · Finances)
├── Branches contextuelles (Matin · Pause · Dîner · Soir)
└── Branches spontanées (idées · intuitions)

Protocole de navigation : ouvrir branche → descendre nœud → remonter nœud → branche parallèle → fermer branche → revenir au tronc
```

## C4.6 — Jeu Blueprint (8 couches)

| # | Nom | Essence |
|---|---|---|
| 1 | La Boucle de Jeu | Jeu cognitif structuré (terminal, évolution étape par étape) |
| 2 | Le Game State Persistant | `.blueprint/state.json` (phase, sous-étape, mode, historique, drapeau complétion) |
| 3 | Le Noyau | Lit état → propose actions → appelle LLM → écrit fichiers → archive → met à jour → recommence |
| 4 | Joueur et Modes | Pilote en mode **manual** (joueur choisit) ou **auto** (Blueprint choisit et exécute) |
| 5 | Monde du Jeu | Fichiers = zones · agents = PNJ · étapes = salles/niveaux |
| 6 | Progression en 4 Niveaux | **Noyau → Pipeline → Agents → Cockpit** (quêtes + boss par niveau) |
| 7 | Condition de Fin | Cockpit V1 fonctionnel → passage en mode surveillance |
| 8 | L'Invariance Ludique | Toute évolution future respecte boucle + progression + rôle joueur-superviseur |

---

# C5 — Phylogénétique cognitive

**Définition** : couche évolutive de l'architecture cognitive. Modélise l'évolution des concepts dans le temps sous forme d'arborescences vivantes (**lignées · familles · mutations · extinctions · émergences**).

**But** : maintenir la cohérence d'une vie entière de cognition en structurant **l'évolution des idées plutôt que leur accumulation brute**.

**Position dans la pile :**
```
C2 (Invariants — éléments stables)
  ↓
C5 (Phylogénie — évolution en branches conceptuelles)
  ↓
C4 (Synthèse — synthèses globales)
```

**Principe** : inspiré de la classification biologique et de la phylogénétique. Chaque concept = organisme cognitif avec :
- ADN conceptuel
- versions successives
- divergences
- lignées

**Fonction** : gérer le volume cognitif massif en créant une phylogénie vivante, intégrée au constructeur global de Blueprint.

**Branches phylogénétiques connues :**
1. Mécanismes d'ancrage (symbolique, invariants, émergences, failles, rôles, relationnel) — **racine de l'arbre**
2. Chronologie de Présence (journées constructives/neutres/effacées, analyse invariants de continuité créative)
3. ADR-001 (arborescence de l'architecture du code)

---

# Méta · Manifeste Blueprint

> Blueprint est un espace où la direction devient claire ; un lieu où la charge mentale chute et la présence revient ; un système qui stabilise ce qui compte et dissout ce qui disperse ; une gravité qui ramène naturellement vers l'essentiel ; une architecture qui transforme la confusion en mouvement ; une navigation qui révèle l'intention implicite et ouvre le bon corridor ; un cycle qui clarifie, stabilise, oriente et ferme proprement ; un attracteur profond qui donne forme à la vie et cohérence au quotidien ; une dynamique qui aligne l'identité, les horizons et les décisions ; un champ qui rend la direction sensible, simple et respirable ; un compagnon qui reformule, recentre et réoriente sans bruit ; un univers où chaque action rapproche de la version la plus juste de soi.

**Site** : askio1.com

**Invariants d'incarnation :**
- Identité : capitaine silencieux, axe invisible, repère stable pour ceux qui n'en ont pas
- Site : montée, silence, bascule, scellement
- Système : pivot qui porte sans pousser
- Relation : calme, directionnelle, non intrusive
- Navigation : **un corridor, pas un menu**

---

# Gaps · À valider · À définir

## Définitions manquantes
- **`d(·, ·)`** : la distance directionnelle est invoquée partout mais jamais typée. Métrique ? pseudo-métrique ? divergence ? → **à formaliser**.
- **`S, O, G, A`** : espaces d'états, observations, buts, actions — cardinalité, structure (continue/discrète), topologie → **à spécifier par domaine d'application**.
- **`α, λ, k`** : paramètres libres. Protocole d'apprentissage ? calibration manuelle ? → **à définir**.
- **`(dF_x)†`** : pseudo-inverse de Moore-Penrose sous-entendu. À confirmer si F est différentiable partout, ou si une version discrète est utilisée.

## Invariants incomplets
- **I5, I27** : absents du corpus. Soit oubliés dans la canonisation, soit jamais définis. **À combler ou retirer** (passer à 26 invariants).

## Surcharge symbolique
- **`A`** utilisé simultanément pour : attracteur (C2), opérateur d'attraction (AGENT-BP-01), espace d'actions (navigation incarnée). **À désambiguïser** — proposer `𝒜` pour espace d'actions, `A(·)` pour opérateur, `A` pour attracteur.

## Architecture implémentation (Phase 2)
- Mapping formel → technique : F ≈ LLM encoder ? G ≈ orchestrateur ? Π ≈ routeur MCP ? A ≈ fine-tuned model ?
- `C_t` en pratique : vecteur d'embedding du contexte ? state JSON ? graphe ?
- `g*` : spec en langage naturel (prompt) ou structure typée (JSON schema) ?

## Empirique (Phase 3)
- Comment mesurer `P(t)`, `H(t)`, `C(t)` en production ?
- Proxy numériques pour `ϟP` (temps de session ≠ présence) ?
- Détection de `τ` (délai directionnel) — signal behavioral ?

---

# Historique

- **v1.0** · 2026-04-15 · Extraction initiale depuis `yoan_import_april.md`. Consolidation C0-C5 + AGENT-BP + FORMULE 29 + phylogénie. Identification des gaps.

---

*Prochaine action suggérée* : **Phase 2** — construire `projects/Blueprint/ARCHITECTURE.md` qui map chaque opérateur formel (F, G, Π, A, C) à son composant technique (LLM frontier, MCP agents, orchestrateur, base vectorielle) pour le site aski01.com.
