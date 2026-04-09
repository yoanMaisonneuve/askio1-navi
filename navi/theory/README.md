# Théorie directionnelle — NAVI / ASKIO1

## Introduction

Ce module formalise la **théorie directionnelle** de NAVI.  
Il relie la dynamique mathématique (équations) à la logique de navigation incarnée.  
Chaque équation correspond à une boucle cognitive ou à un invariant du système ASKIO1.

---

## Structure du dossier

```
navi/theory/
│
├── equations.md        # équations formelles (LaTeX)
├── invariants.py       # constantes directionnelles
├── dynamics.py         # version scalaire (simplifiée)
├── dynamics_vector.py  # version vectorielle (embeddings)
├── text_encoder.py     # encodeur factice pour tests
```

---

## Fondements mathématiques

### 1. Dynamique canonique

$$x_{t+1} = G(A(F(x_t) + (dF_{x_t})^{\dagger}(g^* - F(x_t)))) + C_{corr}(t) + C_{sync}(t) + \varepsilon(t)$$

- **xₜ** : état directionnel à l'instant t
- **A** : attracteur actif (but profond)
- **F(xₜ)** : lecture d'état
- **g\*** : but actif
- **G** : opérateur global (non-linéarité, transformation)
- **C_corr**, **C_sync** : corrections locales et synchronisations collectives
- **ε(t)** : perturbation stochastique

Cette équation est la **base de la navigation incarnée** : elle décrit comment un état se transforme pour réduire la distance à l'attracteur.

---

### 2. Dérive implicite

$$\tau = \frac{dD(x, A)}{dt}$$

- Mesure la **vitesse de dérive** hors du corridor.
- Si τ augmente → dérive cognitive → activation de correction.
- Si τ diminue → stabilisation → maintien du corridor.

---

### 3. Charge mentale

$$C(t) = \int_0^t \| \nabla_x D(x, A) \| \, dt$$

- Quantifie la **surcharge directionnelle**.
- Plus C(t) est élevé, plus le système doit simplifier et fermer.
- Sert de régulateur automatique dans la boucle BNGUR-04.

---

### 4. Stabilisation de présence

$$ϟP(t) = P(t) \cdot H(t) \cdot e^{-\alpha C(t)} \cdot M_\tau(t)$$

- Combine présence, attention, charge mentale et dérive.
- Si ϟP(t) baisse → déclenche stabilisation ou fermeture.
- Si ϟP(t) reste stable → maintien du corridor actif.

---

### 5. Convergence vers l'attracteur profond

$$\frac{dx}{dt} = -\nabla_x D(x, A_{profond}) + \varepsilon(t)$$

- Formalise la **gravité directionnelle** : le mouvement naturel vers la clarté.
- C'est la loi de convergence asymptotique du système.

---

## Implémentation dans NAVI

| Module | Fonction | Équation associée |
|--------|----------|-------------------|
| `clarifier` | Lecture d'état et extraction d'intention | F(xₜ) |
| `stabilizer` | Régulation de présence et charge mentale | ϟP(t), C(t) |
| `navigator` | Sélection du corridor directionnel | τ |
| `integrator` | Mise à jour de l'attracteur | A₀ |
| `converger` | Fermeture et convergence | dx/dt |

---

## Version vectorielle (embeddings)

Les équations sont implémentées sous forme de fonctions vectorielles dans `dynamics_vector.py`.  
Chaque texte est converti en vecteur via `text_to_vec()` pour simuler un embedding directionnel.

```python
from navi.theory.text_encoder import text_to_vec
from navi.theory.dynamics_vector import drift_vec, mental_load_vec

x_t    = text_to_vec("Je suis dispersé.")
x_next = text_to_vec("Je retrouve ma clarté.")
A      = text_to_vec("Clarté, stabilité, direction.")

tau = drift_vec(x_t, A, x_next)
C   = mental_load_vec([x_t, x_next], A)
```

---

## Logique directionnelle

La navigation incarnée suit un cycle stable :

**Lecture → Clarification → Stabilisation → Navigation → Fermeture → Intégration → Convergence**

Chaque boucle correspond à une équation.  
Le système entier transforme la **confusion en direction**.

---

## Tests et validation

```bash
python tests/test_dynamics_vector.py
```

Valide : cohérence des dérives (τ) · stabilité de la charge mentale (C) · similarité avec attracteur (cosine).

---

## Prochaines extensions

- Encodeur réel (transformer ou CLIP)
- Visualisation des trajectoires directionnelles
- Simulation multi-agents (BNGUR-07)
- Intégration cockpit ASKIO1

---

```
ASKIO1 — NAVI / Blueprint
Théorie directionnelle du tout
© 2026 Yoan Maisonneuve
```
