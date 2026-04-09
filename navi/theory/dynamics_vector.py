"""
Dynamique directionnelle de NAVI / ASKIO1 — version vectorielle.

Même équations que dynamics.py, mais opérant sur des vecteurs (embeddings).
Compatible avec text_to_vec() de text_encoder.py.
"""

from typing import List
import math


def distance_vec(x: List[float], A: List[float]) -> float:
    """
    D(x, A) — distance euclidienne entre deux vecteurs.
    """
    return math.sqrt(sum((xi - ai) ** 2 for xi, ai in zip(x, A)))


def drift_vec(x_t: List[float], A: List[float], x_next: List[float]) -> float:
    """
    τ = dD(x, A)/dt ≈ D(x_{t+1}, A) - D(x_t, A)
    Positif → dérive. Négatif → rapprochement de l'attracteur.
    """
    return distance_vec(x_next, A) - distance_vec(x_t, A)


def mental_load_vec(trajectory: List[List[float]], A: List[float]) -> float:
    """
    C(t) = ∫ ||∇_x D(x, A)|| dt
    Version discrète vectorielle.
    """
    if len(trajectory) < 2:
        return 0.0
    total = 0.0
    for i in range(len(trajectory) - 1):
        d1 = distance_vec(trajectory[i], A)
        d2 = distance_vec(trajectory[i + 1], A)
        total += abs(d2 - d1)
    return total


def presence_stabilization_vec(
    P_t: float,
    H_t: float,
    x_t: List[float],
    A: List[float],
    M_tau_t: float,
    alpha: float = 0.1,
) -> float:
    """
    ϟP(t) = P(t) · H(t) · e^{-αC(t)} · M_τ(t)
    C(t) estimé à partir de la distance courante à l'attracteur.
    """
    C_t = distance_vec(x_t, A)
    return P_t * H_t * math.exp(-alpha * C_t) * M_tau_t
