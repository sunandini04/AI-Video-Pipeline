

import os

def create_subtitles_from_speech(speech_text, srt_path, words_per_segment=10, sec_per_segment=5):
    """
    Create a simple SRT file from speech text.
    """
    os.makedirs(os.path.dirname(srt_path), exist_ok=True)

    words = speech_text.split()
    segments = [words[i:i+words_per_segment] for i in range(0, len(words), words_per_segment)]

    with open(srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(segments):
            start_sec = i * sec_per_segment
            end_sec = start_sec + sec_per_segment
            start = f"{start_sec//3600:02}:{(start_sec%3600)//60:02}:{start_sec%60:02},000"
            end = f"{end_sec//3600:02}:{(end_sec%3600)//60:02}:{end_sec%60:02},000"
            f.write(f"{i+1}\n{start} --> {end}\n{' '.join(segment)}\n\n")
