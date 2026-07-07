"""
Translation utilities using deep-translator.

Stock-CIO
"""

from deep_translator import GoogleTranslator


def _contains_korean(text: str) -> bool:
    """Return True if text contains Hangul characters."""
    if not text:
        return False
    return any("\uac00" <= ch <= "\ud7a3" for ch in text)


def translate_text(text: str, target: str = "ko") -> str:
    """Translate given text to `target` language using GoogleTranslator.

    If text already contains Korean (Hangul) we return it unchanged.
    On any error we return the original text to avoid breaking output.
    """
    try:
        if not text or _contains_korean(text):
            return text

        return GoogleTranslator(source="auto", target=target).translate(
            text
        )
    except Exception:
        return text
