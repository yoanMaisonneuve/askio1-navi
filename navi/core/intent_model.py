class IntentModel:
    """
    Modèle d'intention directionnel.
    Analyse le texte et extrait l'intention sous-jacente.
    """

    def extract(self, text: str) -> str:
        text = text.lower()

        if any(w in text for w in ["bloqué", "perdu", "dispersé", "perdue"]):
            return "Retrouver la direction"

        if any(w in text for w in ["objectif", "projet", "but", "ambition"]):
            return "Clarifier l'objectif"

        if any(w in text for w in ["peur", "stress", "anxieux", "anxieuse", "débordé"]):
            return "Réduire la charge mentale"

        if any(w in text for w in ["choisir", "décider", "hésiter", "dilemme"]):
            return "Prendre une décision cohérente"

        if any(w in text for w in ["avancer", "progresser", "bouger", "commencer"]):
            return "Passer à l'action"

        return "Avancer avec clarté"
