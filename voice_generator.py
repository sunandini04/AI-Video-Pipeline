import edge_tts
import asyncio
import os

OUTPUT_AUDIO_PATH = "output/voice.wav"

async def generate_voice(script_text, output_path=OUTPUT_AUDIO_PATH):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    communicate = edge_tts.Communicate(
        text=script_text,
        voice="en-US-AriaNeural"
    )
    await communicate.save(output_path)
    return output_path  

def text_to_speech(script_text):
    """
    Generates voice from text and returns the saved audio path.
    """
    path = asyncio.run(generate_voice(script_text))
    return path
