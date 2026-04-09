def clean_text(text: str) -> str:
    """
    Nettoyage minimal du texte pour réduire le bruit.
    """
    return text.strip().replace("\n", " ").replace("  ", " ")
