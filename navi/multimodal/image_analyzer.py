class ImageAnalyzer:
    """
    Analyseur d'image directionnel.
    Détecte des signaux visuels et les traduit en intention.
    """

    def analyze(self, image_path: str) -> str:
        if not image_path:
            return None

        path = image_path.lower()

        if any(w in path for w in ["messy", "chaos", "disorder"]):
            return "Besoin d'ordre et de clarté"

        if any(w in path for w in ["road", "path", "corridor", "chemin"]):
            return "Recherche de direction"

        if any(w in path for w in ["desk", "bureau", "work", "travail"]):
            return "Organisation du travail"

        if any(w in path for w in ["nature", "calm", "forest", "water"]):
            return "Retour au calme"

        return None
