"""
Tests unitaires pour la dynamique vectorielle de NAVI / ASKIO1.
Valide :
- dérive implicite τ
- charge mentale C(t)
- similarité avec attracteur
- cohérence des embeddings factices
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from navi.theory.text_encoder import text_to_vec, similarity
from navi.theory.dynamics_vector import drift_vec, mental_load_vec


def test_drift_and_load():
    x_t    = text_to_vec("Je suis dispersé et je veux retrouver ma direction.")
    x_next = text_to_vec("Je retrouve ma clarté et je me stabilise.")
    A      = text_to_vec("Clarté, stabilité, direction.")

    tau = drift_vec(x_t, A, x_next)
    C   = mental_load_vec([x_t, x_next], A)

    print(f"Dérive τ         = {tau:.3f}")
    print(f"Charge mentale C = {C:.3f}")

    assert isinstance(tau, float)
    assert isinstance(C, float)
    assert abs(tau) < 2.0
    assert C >= 0.0


def test_similarity():
    v1 = text_to_vec("direction")
    v2 = text_to_vec("orientation")
    v3 = text_to_vec("chaos")

    sim12 = similarity(v1, v2)
    sim13 = similarity(v1, v3)

    print(f"Similarité(direction, orientation) = {sim12:.3f}")
    print(f"Similarité(direction, chaos)       = {sim13:.3f}")

    assert 0.0 <= sim12 <= 1.0
    assert 0.0 <= sim13 <= 1.0
    assert sim12 > sim13  # cohérence sémantique attendue


if __name__ == "__main__":
    print("=== Test dynamique vectorielle NAVI ===")
    test_drift_and_load()
    test_similarity()
    print("=== Tous les tests passés ===")
