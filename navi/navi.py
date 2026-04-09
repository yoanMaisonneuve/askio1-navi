from navi.core.state import State
from navi.clarifier.clarifier import Clarifier
from navi.stabilizer.stabilizer import Stabilizer
from navi.navigator.navigator import Navigator
from navi.video_generator import VideoGenerator
from navi.closer.closer import Closer
from navi.integrator.integrator import Integrator
from navi.redirector.redirector import Redirector
from navi.converger.converger import Converger


class NAVI:
    """
    NAVI v0.4 — Agent directionnel multimodal.

    Pipeline : Clarifier → Stabilizer → Navigator → VideoGenerator
               → Closer → Integrator → Redirector → Converger

    Applique les 7 opérations directionnelles d'ASKIO1.
    """

    def __init__(self, video_backend: str = "skyreels"):
        self.clarifier = Clarifier()
        self.stabilizer = Stabilizer()
        self.navigator = Navigator()
        self.video = VideoGenerator(backend=video_backend)
        self.closer = Closer()
        self.integrator = Integrator()
        self.redirector = Redirector()
        self.converger = Converger()

    def run(self, text: str, image: str = None, audio: str = None):
        state = State(text, image, audio)

        for module in [
            self.clarifier,
            self.stabilizer,
            self.navigator,
            self.video,
            self.closer,
            self.integrator,
            self.redirector,
            self.converger,
        ]:
            state = module.process(state)

        return state.output, state.video_output
