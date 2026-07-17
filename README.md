# 🏋️‍♂️ AI Real-Time Gym Coach

Real-time pose detection with proactive AI voice coaching — built with Streamlit, MediaPipe, and Groq LLM.

An AI-powered gym trainer that watches your workout through your webcam, tracks your reps and form live, and gives you short, energetic voice feedback like a real coach — all without any wearable or manual logging.

Built by **Vishesh Gaur**.

---

## ✨ Features

- **Real-time pose detection** using MediaPipe Pose Landmarker
- **Automatic rep counting** for 5 exercises:
  - Squats
  - Push-ups
  - Biceps Curls (Dumbbell)
  - Shoulder Press
  - Lunges
- **Live form correction** — detects issues like poor depth, back arching, hip sagging, elbow drifting, and torso swinging
- **AI voice coaching** powered by Groq (Llama 3.3 70B) + Google Text-to-Speech, giving short, natural spoken feedback during your set
- **Workout tracking** — sets, reps, and progress saved per user in a local SQLite database
- **Workout history dashboard** with daily aggregated stats
- **Simple username-based login** — no signup required

---

## 🛠️ Tech Stack

| Layer            | Tool/Library                          |
|-------------------|----------------------------------------|
| UI / App Framework | Streamlit                             |
| Live Video         | streamlit-webrtc                      |
| Pose Detection     | MediaPipe (Pose Landmarker)           |
| Image Processing   | OpenCV                                |
| AI Coaching (LLM)  | Groq API (Llama 3.3 70B Versatile)    |
| Text-to-Speech     | gTTS (Google Text-to-Speech)          |
| Database           | SQLite                                |

---

## 📂 Project Structure

```
AI-REAL-TIME-GYM-COACH/
├── main.py                          # App entry point (Streamlit UI + flow)
├── core/
│   └── base_exercise.py             # Shared angle-calculation logic for all detectors
├── detectors/                       # Per-exercise rep counting & form detection
│   ├── squat.py
│   ├── pushup.py
│   ├── biceps_curl.py
│   ├── shoulder_press.py
│   └── lunges.py
├── services/
│   ├── auth/                        # Simple username login wall
│   ├── coaching/                    # LLM + TTS + voice pipeline logic
│   ├── config/                      # Exercise options, prompts, metric field definitions
│   ├── persistence/                 # SQLite read/write helpers
│   ├── state/                       # Streamlit session state defaults
│   ├── tracking/                    # Live metrics syncing between video + UI
│   ├── ui/                          # CSS/font/style injection helpers
│   └── vision/                      # Webcam frame processor (MediaPipe + overlays)
├── ml_models/
│   └── pose_landmarker_full.task    # MediaPipe pose model
├── static/                          # CSS and font assets
├── data.db                          # SQLite database (auto-created)
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd AI-REAL-TIME-GYM-COACH
```

### 2. Create a virtual environment (Python 3.12 recommended)
```bash
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1      # Windows
source .venv/bin/activate       # macOS/Linux
```

### 3. Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set up your Groq API key
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```
> Get a free API key at [console.groq.com](https://console.groq.com)

### 5. Run the app
```bash
streamlit run main.py
```

---

## 🎯 How It Works

1. Log in with a unique username.
2. Choose your exercise, number of sets, and reps per set.
3. Click **Start Workout** — your webcam feed opens with a live skeleton overlay.
4. MediaPipe tracks your joints frame-by-frame; each exercise detector calculates joint angles to count reps and flag form issues.
5. The AI coach gives short voice feedback at key moments — starting the workout, completing a set, correcting your form, and finishing the workout.
6. Your reps, sets, and time are saved automatically, viewable in the **Workout History** section.

---

## 📌 Notes

- Requires a working webcam and browser microphone/camera permissions (camera only — no audio input is used).
- Voice feedback requires an active internet connection (Groq API + Google TTS).
- `.env` and `.venv/` are excluded from version control — never commit your API key.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or raise an issue.

---

## 👤 Author

**Vishesh Gaur**

---

## 📄 License

Copyright © 2026 Vishesh Gaur. All rights reserved.

This project is open source and available for personal and educational use.