from navi.theory.invariants import EQUATIONS


class State:
    """
    Représente l'état directionnel multimodal de NAVI.
    Chaque instance porte les équations directionnelles comme invariants vivants.
    """

    def __init__(self, text: str, image: str = None, audio: str = None):
        self.equations = EQUATIONS  # invariants directionnels
        self.input = text
        self.image = image
        self.audio = audio

        self.intent = None
        self.stabilized = None
        self.direction = None
        self.closure = None
        self.integration = None
        self.redirection = None
        self.convergence = None

        self.video_prompt = None
        self.video_output = None
        self.output = None
