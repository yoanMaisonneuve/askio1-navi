import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from navi.navi import NAVI

agent = NAVI()

# Cas 1 — texte seul
print("=== Cas 1 : texte seul ===")
output, video = agent.run("Je suis dispersé et je veux retrouver ma direction.")
print(output)
if video:
    print(f"\nVidéo : {video}")

print()

# Cas 2 — texte + image + audio
print("=== Cas 2 : multimodal ===")
output, video = agent.run(
    "Je veux clarifier mon objectif pour avancer.",
    image="desk.jpg",
    audio="calm_voice.wav",
)
print(output)
if video:
    print(f"\nVidéo : {video}")
