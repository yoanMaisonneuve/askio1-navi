class Attractor:
    """
    Attracteur directionnel A₀.
    Point fixe vers lequel NAVI ramène l'état.
    """

    def __init__(self, label: str = "essentiel"):
        self.label = label

    def distance(self, state) -> float:
        """
        Mesure symbolique de la distance à l'attracteur.
        Retourne 0.0 si aligné, 1.0 si en dérive totale.
        """
        if state.intent and state.direction:
            return 0.2
        if state.intent:
            return 0.5
        return 1.0

    def __repr__(self):
        return f"Attractor(A₀={self.label})"
