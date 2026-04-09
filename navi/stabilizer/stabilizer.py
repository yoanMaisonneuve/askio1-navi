class Stabilizer:
    """
    Opération 2 : Stabilisation.
    Réduit le bruit et stabilise la présence autour de l'intention.
    """

    def process(self, state):
        state.stabilized = f"Présence stabilisée autour de : {state.intent}"
        return state
