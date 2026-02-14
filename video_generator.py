import os
from moviepy import VideoFileClip, AudioFileClip, vfx


def create_video_with_audio(video_path, audio_path, output_path):

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    audio_duration = audio.duration
    video_duration = video.duration

   
    if video_duration < audio_duration:
        video = video.with_effects([vfx.Loop(duration=audio_duration)])

   
    final_video = video.subclipped(0, audio_duration)

    
    final_video = final_video.with_audio(audio)

    
    final_video.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac"
    )

    
    video.close()
    audio.close()
    final_video.close()

    return output_path
