import edge_tts
import asyncio
import os

def get_audio_path(topic):
    safe_topic = topic.replace(" ", "_")
    return f"output/{safe_topic}_voice.wav"


async def generate_voice(script_text, voice, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    communicate = edge_tts.Communicate(
        text=script_text,
        voice=voice
    )

    await communicate.save(output_path)
    return output_path


def text_to_speech(script_text, voice,topic):
    """
    Generates voice from text using selected language voice.
    """
    output_path = get_audio_path(topic)
    path = asyncio.run(generate_voice(script_text, voice,output_path))
    return path
