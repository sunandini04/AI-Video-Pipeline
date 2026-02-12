

# 🎬 AI Video Generation Pipeline

An end-to-end automated AI-powered pipeline that converts a **topic input** into a **YouTube-ready video** using free tools and APIs.

One trigger → One complete video.

---

## 🚀 Overview

This project builds a fully automated AI video generation system using Python.

Given a topic, the pipeline:

1. Generates an AI script
2. Converts the script to AI voiceover
3. Fetches relevant visuals
4. Merges everything into a final `.mp4` video
5. Automatically generates subtitles

The entire flow runs with a single command.

---

## 🏗️ Architecture

```
User Input (Topic)
        ↓
Script Generation (Gemini / AI API)
        ↓
Speech Cleaning (Remove comments, hashtags)
        ↓
Text-to-Speech (Edge TTS)
        ↓
Visual Fetching (Pexels API)
        ↓
Video + Audio Merge (MoviePy)
        ↓
Subtitle Generation (.srt)
        ↓
Final YouTube-ready Video (.mp4)
```

---

## 🛠️ Tech Stack

* **Python**
* **Gemini / AI API** – Script generation
* **Edge TTS** – AI voiceover
* **Pexels API** – Stock video visuals
* **MoviePy** – Video + audio merging
* **FFmpeg** – Subtitle burning
* **Requests** – API handling

All tools used are free-tier compatible.

---

## 📂 Project Structure

```
main.py
script_generator.py
voice_generator.py
video_generator.py
visuals_fetcher.py
script_utils.py
subtitle_utils.py
requirements.txt
README.md
```

---

## ⚙️ How to Run

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Add API keys

Create a `.env` file:

```
PEXELS_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```

### 3️⃣ Run the pipeline

```
python main.py
```

Enter a topic when prompted.

The final video will be generated inside the `output/` folder.

---

## 🎥 Output

For topic:
`AI in Business`

Generated files:

```
AI_in_Business.mp4
AI_in_Business.srt
voice.wav
```

The final `.mp4` is YouTube-ready.

---

## 🔥 Key Features

* Fully automated pipeline
* Cleans AI-generated script before voice generation
* Dynamic video naming (avoids overwrite)
* Subtitle generation and embedding
* One-command execution

---

## 🧠 Technical Decisions

* Separated speech from script comments to prevent narration errors
* Used FFmpeg for reliable subtitle burning
* Ensured audio duration sync with video duration
* Modular architecture for scalability

---

## 📈 Future Improvements

* Dynamic scene-level visual switching
* Background music automation
* Auto-thumbnail generation
* Direct YouTube upload via API
* SEO metadata auto-generation

---

## 📌 Evaluation Focus

This project emphasizes:

* End-to-end automation
* Clean architecture
* Modular code structure
* Practical AI integration

---

## 👩‍💻 Author

**Sunandini Das**
B.Tech CSE



