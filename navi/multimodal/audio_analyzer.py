class AudioAnalyzer:
    """
    Analyseur audio directionnel.
    Détecte des signaux émotionnels et les traduit en intention.
    """

    def analyze(self, audio_path: str) -> str:
        if not audio_path:
            return None

        path = audio_path.lower()

        if any(w in path for w in ["stress", "tension", "fast", "rapid"]):
            return "Réduire la charge mentale"

        if any(w in path for w in ["calm", "slow", "soft", "calme"]):
            return "Stabilisation déjà en cours"

        if any(w in path for w in ["sad", "low", "triste"]):
            return "Retrouver la direction"

        return None
