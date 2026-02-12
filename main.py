
from script_generator import generate_script
from voice_generator import text_to_speech
from video_generator import create_video_with_audio
from visuals_fetcher import fetch_video_from_pexels
from script_utils import extract_speech
from subtitle_utils import create_subtitles_from_speech
import os
import subprocess

def main():
    topic = input("Enter video topic: ")
    safe_topic = topic.replace(" ", "_")

    os.makedirs("output", exist_ok=True)

    print("Generating script...")
    script = generate_script(topic)

    print("\n--- GENERATED SCRIPT ---\n")
    print(script)

    speech_text = extract_speech(script)

    print("\nGenerating voice...")
    audio_path = text_to_speech(speech_text)

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
        "-vf", f"subtitles={subtitle_path}",
        "-c:a", "copy",
        temp_video
    ]

    subprocess.run(command, check=True)

    os.remove(final_video_path)
    os.rename(temp_video, final_video_path)

    print(f"\n Final Video: {final_video_path}")
    print(f" Subtitle File: {subtitle_path}")
    print(f" Voice File: {audio_path}")

if __name__ == "__main__":
    main()
