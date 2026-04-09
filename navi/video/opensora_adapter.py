class OpenSoraAdapter:
    """
    Adaptateur pour Open-Sora.
    Prêt à recevoir l'intégration modèle réelle.
    """

    def generate(self, prompt: str) -> str:
        # TODO: intégrer Open-Sora (local ou API)
        return f"[Open-Sora] Vidéo générée pour : {prompt}"
