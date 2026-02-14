

# 🎬 AI-Powered Multilingual Video Generation Engine

An end-to-end automated **production-grade AI pipeline** that converts a single topic into a fully YouTube-ready video — complete with voiceover, subtitles, thumbnail, and sync optimization.

One trigger → One complete AI-produced video.

---

## 🚀 Overview

This project builds a fully automated AI video generation system using Python.

Given a topic, the pipeline:

1. Generates an AI-optimized script
2. Cleans narration artifacts automatically
3. Detects language dynamically
4. Generates AI voice with safe fallback
5. Fetches relevant AI-matched visuals
6. Sync-optimizes video with audio duration
7. Generates clean subtitles (.srt)
8. Creates an auto thumbnail
9. Outputs a production-ready `.mp4`

All with a single command.

---

## 🏗️ Production Architecture

```
User Topic Input
        ↓
AI Script Generation (Gemini API)
        ↓
Script Cleaning Engine
        ↓
Dynamic Language Detection
        ↓
AI Voice Generation (Edge TTS / Fallback)
        ↓
Visual Fetching Engine (Pexels API)
        ↓
Sync-Optimized Video Rendering (MoviePy)
        ↓
Subtitle Generation (.srt)
        ↓
Auto Thumbnail Generator
        ↓
Final YouTube-Ready Video (.mp4)
```

---

## 🛠️ Tech Stack

* **Python**
* **Gemini API** – Intelligent script generation
* **Edge TTS** – Multilingual AI voice engine
* **Pexels API** – Context-aware visual fetching
* **MoviePy** – Audio-video merging & timing control
* **FFmpeg** – Subtitle embedding & processing
* **Requests** – API handling
* **Lang Detection Logic** – Dynamic voice language switching

All tools are free-tier compatible.

---

## 📂 Project Structure

```
main.py
language_utils.py
script_generator.py
voice_generator.py
video_generator.py
visuals_fetcher.py
script_utils.py
subtitle_utils.py
thumbnail_generator.py
README.md
```

---

## ⚙️ How to Run

###  

### 1️⃣ Add API Keys

Create a `.env` file:

```
PEXELS_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```

### 2️⃣Run the Engine

```
python main.py
```

Enter your topic when prompted.

---

## 🎥 Output Structure

All files are generated inside:

```
output/
    video.mp4
    voice.wav
    video.srt
    thumbnail.jpg
```

✔ Clean
✔ Structured
✔ No clutter
✔ Production-safe

---

## 🔥 Core Features

* 🔹 Dynamic multilingual voice detection
* 🔹 Clean subtitle generation
* 🔹 Auto thumbnail generation
* 🔹 Audio-video duration synchronization
* 🔹 Safe fallback if TTS fails
* 🔹 Error-handled production flow
* 🔹 Centralized output management

---

## 🧠 Engineering Decisions

* Separated script cleaning from script generation to avoid narration artifacts
* Centralized output structure to prevent naming conflicts
* Implemented sync optimization to avoid audio-video mismatch
* Added try/except blocks for production-level stability
* Modular architecture for scalability

---

## 🛡️ Error Handling System

The system gracefully handles:

* Voice generation failure
* API timeout issues
* Visual fetching errors
* Audio sync mismatches

Fallback mechanisms ensure video generation continues even if a component fails.

---

## 🌍 Example Test Topic

Try:

```
AI in Animation
YouTube: https://www.youtube.com/watch?v=YFhDnkiyZRI
```

This tests:

* Multilingual compatibility
* Dynamic script cleaning
* Sync optimization
* Thumbnail generation
* Error-safe voice generation

---

## 📈 Future Enhancements

* Scene-level AI visual segmentation
* Background music auto-balancing
* Direct YouTube API upload
* SEO metadata generation
* AI-based hook optimization

---

## 📌 Project Focus

This project demonstrates:

* End-to-end AI automation
* Production-grade error handling
* Modular scalable architecture
* Practical AI integration
* Real-world deployment readiness

---



**Sunandini Das**
B.Tech CSE





