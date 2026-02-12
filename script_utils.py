import re

def extract_speech(script_text):
    
    script_text = re.sub(r"\(.*?\)", "", script_text)

    lines = script_text.split("\n")
    cleaned = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("#"):
            continue

        if line.lower().startswith("b-roll"):
            continue

        cleaned.append(line)

    return "\n".join(cleaned)
