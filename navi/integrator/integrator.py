class Integrator:
    """
    Opération 5 : Intégration.
    Met à jour l'attracteur selon la direction choisie.
    """

    def process(self, state):
        state.integration = f"Attracteur mis à jour selon : {state.direction}"
        return state
