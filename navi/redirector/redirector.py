class Redirector:
    """
    Opération 6 : Redirection.
    Ramène à l'essentiel. Élimine la dérive résiduelle.
    """

    def process(self, state):
        state.redirection = "Retour à l'essentiel effectué"
        return state
