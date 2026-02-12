import os
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips

def create_video_with_audio(video_path, audio_path, output_path):

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    clips = []
    total_duration = 0

    while total_duration < audio.duration:
        clips.append(video)
        total_duration += video.duration

    final_video = concatenate_videoclips(clips)

    final_video = final_video.subclipped(0, audio.duration)

    final_video = final_video.with_audio(audio)

    final_video.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac"
    )

    return output_path
