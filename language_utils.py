import edge_tts
import asyncio

DEFAULT_VOICE = "en-US-AriaNeural"

LANGUAGE_CODES = {
    "english": "en",
    "hindi": "hi",
    "bengali": "bn",
    "japanese": "ja",
    "korean": "ko",
    "chinese": "zh",
    "spanish": "es",
    "french": "fr",
    "german": "de",
    "italian": "it",
    "russian": "ru",
    "arabic": "ar"
}


async def find_voice_for_language(language_name):
    language_name = language_name.lower()
    iso_code = LANGUAGE_CODES.get(language_name)

    if not iso_code:
        print("Language not recognized. Falling back to English.")
        return DEFAULT_VOICE

    voices = await edge_tts.list_voices()

    for voice in voices:
        if voice["Locale"].startswith(iso_code):
            return voice["Name"]

    print("No matching voice found. Falling back to English.")
    return DEFAULT_VOICE


def get_voice(language_name):
    return asyncio.run(find_voice_for_language(language_name))


def get_language_prompt(language_name):
    return f"Write the script in {language_name}."
