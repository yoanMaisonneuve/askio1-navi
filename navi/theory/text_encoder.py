"""
Encodeur factice pour NAVI / ASKIO1.
Transforme un texte en vecteur numérique simple, sans modèle externe.
Remplaçable par un vrai encoder (transformer, CLIP, etc.) sans changer l'interface.
"""

import math
from typing import List


def text_to_vec(text: str, dim: int = 8) -> List[float]:
    """
    Encodeur factice : convertit un texte en vecteur de taille `dim`.
    - Utilise le hash des caractères pour générer une signature stable.
    - Normalise le vecteur (L2) pour éviter les valeurs extrêmes.
    """
    text = text.lower().strip()
    base = [0.0] * dim

    for i, ch in enumerate(text):
        base[i % dim] += (ord(ch) % 97) / 100.0

    norm = math.sqrt(sum(v ** 2 for v in base)) or 1.0
    return [v / norm for v in base]


def similarity(v1: List[float], v2: List[float]) -> float:
    """
    Cosine similarity entre deux vecteurs.
    Retourne 1.0 si identiques, 0.0 si orthogonaux.
    """
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a ** 2 for a in v1))
    norm2 = math.sqrt(sum(b ** 2 for b in v2))
    return dot / (norm1 * norm2 + 1e-9)
