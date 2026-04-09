from navi.theory.dynamics import drift, mental_load


class Stabilizer:
    """
    Opération 2 : Stabilisation.
    Réduit le bruit et stabilise la présence autour de l'intention.
    Utilise les équations de dérive (τ) et charge mentale (C).
    """

    def process(self, state):
        # x = niveau de dispersion scalaire (1.0 = dispersé, 0.0 = centré)
        x_t    = 1.0
        x_next = 0.7
        A      = 0.0  # attracteur = état de clarté

        tau = drift(x_t, A, x_next)
        C   = mental_load([x_t, x_next], A)

        state.stabilized = (
            f"Présence stabilisée (τ={tau:.3f}, C={C:.3f}) autour de : {state.intent}"
        )
        return state
