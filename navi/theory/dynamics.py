"""
Dynamique directionnelle de NAVI / ASKIO1 — version scalaire.

Implémente des versions opérationnelles (discrètes, simplifiées) de :
- dérive implicite τ
- charge mentale C(t)
- stabilisation de présence ϟP(t)
- dynamique canonique x_{t+1}
"""

from typing import List, Callable
import math


def distance(x: float, A: float) -> float:
    """
    D(x, A) — distance directionnelle simplifiée (scalaire).
    """
    return abs(x - A)


def drift(x_t: float, A: float, x_next: float) -> float:
    """
    τ = dD(x, A)/dt ≈ D(x_{t+1}, A) - D(x_t, A)
    Positif → dérive. Négatif → stabilisation.
    """
    return distance(x_next, A) - distance(x_t, A)


def mental_load(trajectory: List[float], A: float) -> float:
    """
    C(t) = ∫ ||∇_x D(x, A)|| dt
    Version discrète : somme des variations de distance.
    """
    if len(trajectory) < 2:
        return 0.0
    total = 0.0
    for i in range(len(trajectory) - 1):
        total += abs(distance(trajectory[i + 1], A) - distance(trajectory[i], A))
    return total


def presence_stabilization(
    P_t: float,
    H_t: float,
    C_t: float,
    M_tau_t: float,
    alpha: float = 0.1,
) -> float:
    """
    ϟP(t) = P(t) · H(t) · e^{-αC(t)} · M_τ(t)
    """
    return P_t * H_t * math.exp(-alpha * C_t) * M_tau_t


def step_dynamics(
    x_t: float,
    G: Callable[[float], float],
    g_star: float,
    C_corr_t: float = 0.0,
    C_sync_t: float = 0.0,
    epsilon_t: float = 0.0,
) -> float:
    """
    x_{t+1} = G(A(F(x_t) + (dF_x_t)†(g* - F(x_t)))) + C_corr(t) + C_sync(t) + ε(t)

    Ici : F = Id, (dF)† = 1, A = Id
    """
    F_xt = x_t
    inner = F_xt + (g_star - F_xt)  # correction directionnelle
    core = G(inner)
    return core + C_corr_t + C_sync_t + epsilon_t
