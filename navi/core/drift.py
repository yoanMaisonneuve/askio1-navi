class DriftDetector:
    """
    Détecte la dérive directionnelle dans le texte.
    Une dérive = distance croissante par rapport à A₀.
    """

    DRIFT_SIGNALS = [
        "je ne sais pas", "je sais plus", "tout s'accumule",
        "impossible", "j'abandonne", "je tourne en rond",
        "rien n'avance", "plus de sens",
    ]

    def detect(self, text: str) -> bool:
        text = text.lower()
        return any(signal in text for signal in self.DRIFT_SIGNALS)

    def score(self, text: str) -> float:
        """
        Score de dérive entre 0.0 (aligné) et 1.0 (dérive totale).
        """
        text = text.lower()
        hits = sum(1 for s in self.DRIFT_SIGNALS if s in text)
        return min(hits / 3, 1.0)
