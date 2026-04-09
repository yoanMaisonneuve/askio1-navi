class VideoPipeline:
    """
    Pipeline vidéo unifié pour NAVI.
    Sélectionne automatiquement le backend (SkyReels, Open-Sora, LTX).
    """

    def __init__(self, skyreels, opensora, ltx):
        self.skyreels = skyreels
        self.opensora = opensora
        self.ltx = ltx

    def generate(self, prompt: str, backend: str = "skyreels"):
        if backend == "skyreels":
            return self.skyreels.generate(prompt)

        if backend == "opensora":
            return self.opensora.generate(prompt)

        if backend == "ltx":
            return self.ltx.generate(prompt)

        raise ValueError(f"Backend vidéo inconnu : {backend}")
