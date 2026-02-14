from script_generator import generate_script
from voice_generator import text_to_speech
from video_generator import create_video_with_audio
from visuals_fetcher import fetch_video_from_pexels
from script_utils import extract_speech
from subtitle_utils import create_subtitles_from_speech
from language_utils import get_voice, get_language_prompt
from thumbnail_generator import generate_thumbnail


import os
import subprocess


def main():
    topic = input("Enter video topic: ")
    language = input("Choose a language: ")

    safe_topic = topic.replace(" ", "_")

    os.makedirs("output", exist_ok=True)

    print("Generating script...")
    language_prompt = get_language_prompt(language)
    script = generate_script(f"{topic}. {language_prompt}")

    print("\n--- GENERATED SCRIPT ---\n")
    print(script)

    speech_text = extract_speech(script)

    print("\nDetecting voice...")
    voice = get_voice(language)

    print("\nGenerating voice...")
    audio_path = text_to_speech(speech_text, voice, topic)

    print("\nFetching visuals from Pexels...")
    video_path = fetch_video_from_pexels(topic)

    final_video_path = f"output/{safe_topic}.mp4"

    print("\nMerging video and audio...")
    create_video_with_audio(video_path, audio_path, final_video_path)

    subtitle_path = f"output/{safe_topic}.srt"
    create_subtitles_from_speech(speech_text, subtitle_path)

    print("Burning subtitles into video...")

    temp_video = f"output/{safe_topic}_temp.mp4"

    command = [
        "ffmpeg",
        "-y",
        "-i", final_video_path,
        "-vf", f"subtitles='{subtitle_path}'",
        "-c:a", "copy",
        temp_video
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print("FFmpeg failed to burn subtitles. Using video without burned subtitles.")


    os.remove(final_video_path)
    os.rename(temp_video, final_video_path)

    print("Generating thumbnail...")
    thumbnail_path = f"output/{safe_topic}_thumbnail.jpg"
    generate_thumbnail(final_video_path, topic, thumbnail_path)


    print(f"\nFinal Video: {final_video_path}")
    print(f"Subtitle File: {subtitle_path}")
    print(f"Voice File: {audio_path}")


if __name__ == "__main__":
    main()
