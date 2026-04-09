class Fusion:
    """
    Fusionne texte + image + audio en une intention multimodale unifiée.
    Priorité : texte > image > audio.
    """

    def fuse(self, text_intent: str, image_intent: str, audio_intent: str) -> str:
        intents = [i for i in [text_intent, image_intent, audio_intent] if i]

        if not intents:
            return "Avancer avec clarté"

        # Le texte est toujours prioritaire — les autres enrichissent
        primary = text_intent or intents[0]
        secondary = [i for i in intents if i != primary]

        if secondary:
            return f"{primary} ({' · '.join(secondary)})"

        return primary
