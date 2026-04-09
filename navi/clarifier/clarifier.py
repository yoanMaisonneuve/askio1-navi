from navi.core.intent_model import IntentModel
from navi.core.text_utils import clean_text
from navi.multimodal.image_analyzer import ImageAnalyzer
from navi.multimodal.audio_analyzer import AudioAnalyzer
from navi.multimodal.fusion import Fusion


class Clarifier:
    """
    Opération 1 : Clarification.
    Extrait l'intention directionnelle depuis le texte, l'image et l'audio.
    """

    def __init__(self):
        self.model = IntentModel()
        self.image = ImageAnalyzer()
        self.audio = AudioAnalyzer()
        self.fusion = Fusion()

    def process(self, state):
        text_intent = self.model.extract(clean_text(state.input))
        image_intent = self.image.analyze(state.image)
        audio_intent = self.audio.analyze(state.audio)

        state.intent = self.fusion.fuse(text_intent, image_intent, audio_intent)
        return state
