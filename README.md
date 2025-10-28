
# 🧠 Talking Assistant

A **voice-controlled AI assistant** inspired by *Talking Tom*, built in **Python**.  
It listens to your voice, understands natural commands using a **local LLM**, performs real-world actions (like opening YouTube or telling time), and replies back with **speech and animation** on a web interface.

---

## 🎯 Features

- 🎙️ **Speech Recognition (STT)** — Understands your voice commands  
- 🧠 **Local LLM Integration** — Uses open-source models like `Phi-3` or `Mistral` via Ollama  
- ⚙️ **Action Executor** — Opens apps, tells time, searches web, etc.  
- 🗣️ **Text-to-Speech (TTS)** — Speaks back responses naturally  
- 🐱 **Animated Web Avatar** — Interacts visually like Talking Tom (coming soon)  
- 🔄 **Modular Architecture** — Easy to add new commands and actions  

---

## 🏗️ Tech Stack

| Component | Tool / Library | Description |
|------------|----------------|--------------|
| **Backend Framework** | Flask + Flask-SocketIO | Web server and real-time communication |
| **Speech Recognition** | SpeechRecognition / Whisper | Converts voice to text |
| **Language Model (LLM)** | Ollama (Phi-3 / Mistral) | Local, fast, open-source model |
| **Text to Speech (TTS)** | pyttsx3 / gTTS | Converts text to voice |
| **Frontend Animation** | Three.js / Rive | 3D or 2D talking avatar |
| **System Actions** | os / subprocess / webbrowser | Executes PC-level commands |

---

## 📁 Folder Structure

```

talking_assistant/
│
├── backend/
│   ├── main.py                # Main Flask backend
│   ├── stt.py                 # Speech-to-text logic
│   ├── tts.py                 # Text-to-speech logic
│   ├── llm_engine.py          # LLM command understanding
│   ├── command_handler.py     # Executes user commands
│   ├── actions/               # Modular action scripts
│   │   ├── open_youtube.py
│   │   ├── open_chrome.py
│   │   └── get_time.py
│   └── utils/
│       └── audio_utils.py     # Helper functions for audio handling
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   │   └── animation.js   # Avatar + mic controls
│   │   └── assets/
│   │       └── avatar.glb     # 3D model or character asset
│   ├── templates/
│   │   └── index.html         # Web interface
│
├── models/
│   ├── whisper/               # Whisper STT models (optional)
│   ├── ollama/                # Ollama LLM configs
│
├── requirements.txt
└── README.md

````

## ▶️ Usage (to be implemented in later phases)

Once Phase 1–6 are complete:

```bash
python backend/main.py
```

Then open the browser:

```
http://127.0.0.1:5000/
```

Click the 🎙️ mic button, speak a command (like “play YouTube”), and watch your assistant respond!

---

## 🧩 Development Roadmap

| Phase | Description                                      | Status |
|-------|--------------------------------------------------|--------|
| 0     | Project setup & environment                      | ✅      |
| 1     | Speech-to-Text (STT)                             | ⏳      |
| 2     | LLM Integration (Intent Understanding)           | ⏳      |
| 3     | Command Handling                                 | ⏳      |
| 4     | Text-to-Speech (TTS)                             | ⏳      |
| 5     | Backend Integration                              | ⏳      |
| 6     | Frontend Talking Avatar                          | ⏳      |
| 7     | Testing & Optimization                           | ⏳      |
| 8     | Optional Features (wake word, personality, etc.) | ⏳      |

---

## 🔮 Future Enhancements

* Wake-word detection (“Hey Tom!”)
* Memory / personality (stores user preferences)
* Emotion-based animations
* Web search integration
* Mobile (PWA / Android) version

---

## 🪪 License

This project is open-source under the **MIT License** — feel free to use and modify for educational and personal projects.

---

> “Build assistants that feel alive — not just functional.” 🐱✨

