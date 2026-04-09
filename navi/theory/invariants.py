"""
Invariants directionnels de NAVI / ASKIO1.
Ces équations sont le cœur du système — pas du code, des lois.
"""

EQUATIONS = {
    "dynamique_canonique": "x_{t+1} = G(A(F(x_t) + (dF_{x_t})†(g* - F(x_t)))) + C_corr(t) + C_sync(t) + ε(t)",
    "attracteur_defaut":   "A₀ = argmax_A T(A)",
    "derive_implicite":    "τ = dD(x, A)/dt",
    "charge_mentale":      "C(t) = ∫₀ᵗ ||∇ₓD(x, A)|| dt",
    "stabilisation_presence": "ϟP(t) = P(t)·H(t)·e^{-αC(t)}·M_τ(t)",
    "convergence_attracteur": "dx/dt = -∇ₓD(x, A_profond) + ε(t)",
}
