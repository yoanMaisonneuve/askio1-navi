from navi.video.pipeline import VideoPipeline
from navi.video.skyreels_adapter import SkyReelsAdapter
from navi.video.opensora_adapter import OpenSoraAdapter
from navi.video.ltx_adapter import LTXAdapter


class VideoGenerator:
    """
    Génère une vidéo si le Navigator a produit un prompt directionnel.
    """

    def __init__(self, backend: str = "skyreels"):
        self.backend = backend
        self.pipeline = VideoPipeline(
            skyreels=SkyReelsAdapter(),
            opensora=OpenSoraAdapter(),
            ltx=LTXAdapter(),
        )

    def process(self, state):
        if state.video_prompt:
            state.video_output = self.pipeline.generate(state.video_prompt, self.backend)
        return state
