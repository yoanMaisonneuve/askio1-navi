# ASKIO1 / NAVI — Système de navigation directionnelle

## Vision

ASKIO1 est un **système de navigation humaine**.  
Un cockpit.  
Un axe.  
Un champ directionnel qui clarifie, stabilise et oriente.

Au centre : **NAVI**, un agent autonome qui comprend l'intention, réduit la charge mentale et ouvre le bon corridor.

---

## Architecture

```
navi/
│
├── core/           # État directionnel et logique interne
├── clarifier/      # Lecture et clarification d'intention
├── stabilizer/     # Régulation de présence et charge mentale
├── navigator/      # Sélection du corridor directionnel
├── closer/         # Fermeture propre des cycles
├── integrator/     # Mise à jour de l'attracteur
├── redirector/     # Retour à l'essentiel
├── converger/      # Convergence et sortie finale
├── video/          # Pipeline vidéo IA (SkyReels / Open-Sora / LTX)
├── multimodal/     # Analyse image + audio + fusion
└── theory/         # Équations directionnelles et invariants
```

---

## Théorie directionnelle

La dynamique de NAVI repose sur un ensemble d'équations formelles décrivant la **navigation incarnée** :

$$x_{t+1} = G(A(F(x_t) + (dF_{x_t})^{\dagger}(g^* - F(x_t)))) + C_{corr}(t) + C_{sync}(t) + \varepsilon(t)$$

Chaque module correspond à une boucle cognitive :

| Module | Équation |
|--------|----------|
| `clarifier` | F(xₜ) — lecture d'état |
| `stabilizer` | ϟP(t), C(t) — régulation de présence |
| `navigator` | τ — dérive implicite |
| `integrator` | A₀ — attracteur |
| `converger` | dx/dt — convergence |

Détails dans [navi/theory/README.md](navi/theory/README.md).

**Catalogue canonique complet** : [docs/EQUATIONS.md](docs/EQUATIONS.md) — référence unique pour C0 (invariants) → C5 (phylogénétique cognitive), incluant AGENT-BP, BNGUR, TNI, PNC-01, FORMULE 29. Toute implémentation doit référencer un ID canonique (ex: `BNGUR-ENGU-01`, `C3.2`, `I17`).

---

## Démarrage rapide

```bash
# Depuis la racine du repo
PYTHONPATH=. python examples/demo.py
```

```
=== Cas 1 : texte seul ===
Intention    : Retrouver la direction
Direction    : Corridor : Recentrage
Convergence  : Convergence vers la version la plus juste

=== Cas 2 : multimodal ===
Intention    : Clarifier l'objectif (Organisation du travail · Stabilisation déjà en cours)
Direction    : Corridor : Clarification
Vidéo        : [SkyReels] Vidéo générée pour : ...
```

---

## Pipeline vidéo IA

NAVI v0.4 introduit la génération vidéo via un pipeline modulaire :

- **SkyReels** — moteur libre de rendu IA
- **Open-Sora** — modèle de génération vidéo open source
- **LTX-Video** — moteur de composition directionnelle

Chaque backend est accessible via `VideoPipeline`.

---

## Tests

```bash
PYTHONPATH=. python tests/test_dynamics_vector.py
```

Valide : dérives (τ) · charge mentale (C) · similarité cosine avec attracteur.

---

## Roadmap (12 mois)

1. **Fondation** — NAVI v0.x + Gravité YouTube
2. **Communauté** — Discord + Feedback Loop
3. **Asymétrie** — NAVI v1.0 + Cockpit ASKIO1
4. **Infrastructure** — API publique + Compute hybride
5. **Écosystème** — Marketplace d'agents
6. **Empire** — Gravité mondiale + Cockpit v2

---

## Liens

- Site : [askio1.com](https://askio1.com)
- Chaîne YouTube : [ASKIO1](https://www.youtube.com/@askio1)
- GitHub : [yoanMaisonneuve/askio1-navi](https://github.com/yoanMaisonneuve/askio1-navi)

---

```
ASKIO1 — NAVI / Blueprint
Théorie directionnelle du tout
© 2026 Yoan Maisonneuve
```
