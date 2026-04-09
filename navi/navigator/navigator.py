class Navigator:
    """
    Opération 3 : Navigation.
    Sélectionne un corridor directionnel et décide si une vidéo est pertinente.
    """

    def process(self, state):
        intent = state.intent

        if "direction" in intent:
            state.direction = "Corridor : Recentrage"
            state.video_prompt = None

        elif "objectif" in intent:
            state.direction = "Corridor : Clarification"
            state.video_prompt = f"Vidéo expliquant l'objectif : {state.input}"

        elif "charge mentale" in intent:
            state.direction = "Corridor : Simplification"
            state.video_prompt = "Vidéo calme et minimaliste"

        elif "décision" in intent:
            state.direction = "Corridor : Choix cohérent"
            state.video_prompt = "Vidéo montrant deux chemins"

        elif "action" in intent:
            state.direction = "Corridor : Activation"
            state.video_prompt = f"Vidéo dynamique basée sur : {state.input}"

        else:
            state.direction = "Corridor : Mouvement"
            state.video_prompt = None

        return state
