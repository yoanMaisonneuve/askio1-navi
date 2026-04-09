class Closer:
    """
    Opération 4 : Fermeture.
    Ferme proprement les cycles ouverts. Une seule direction retenue.
    """

    def process(self, state):
        state.closure = "Fermeture propre : une seule direction retenue"
        return state
