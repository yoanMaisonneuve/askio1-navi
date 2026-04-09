class LoadEstimator:
    """
    Estime la charge mentale à partir du texte.
    Charge = nombre de cycles ouverts non résolus.
    """

    LOAD_SIGNALS = [
        "et aussi", "en plus", "il faut aussi", "sans oublier",
        "j'ai aussi", "à gérer", "pas encore", "toujours pas",
        "n'oublie pas", "je dois encore",
    ]

    def estimate(self, text: str) -> float:
        """
        Retourne un score de charge entre 0.0 (légère) et 1.0 (maximale).
        """
        text = text.lower()
        hits = sum(1 for s in self.LOAD_SIGNALS if s in text)
        return min(hits / 5, 1.0)

    def label(self, score: float) -> str:
        if score < 0.3:
            return "Charge légère"
        if score < 0.6:
            return "Charge modérée"
        return "Charge élevée"
