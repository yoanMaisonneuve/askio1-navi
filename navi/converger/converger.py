class Converger:
    """
    Opération 7 : Convergence.
    Produit la sortie finale — la version la plus juste de l'état.
    """

    def process(self, state):
        state.convergence = "Convergence vers la version la plus juste"
        state.output = (
            f"Intention    : {state.intent}\n"
            f"Stabilisation: {state.stabilized}\n"
            f"Direction    : {state.direction}\n"
            f"Fermeture    : {state.closure}\n"
            f"Intégration  : {state.integration}\n"
            f"Redirection  : {state.redirection}\n"
            f"Convergence  : {state.convergence}"
        )
        return state
