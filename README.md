tts-project/
 ├── api.py
 ├── Dockerfile
 ├── requirements.txt
 ├── README.md 

 🎤 Multilingual Text-to-Speech API (TTS)
📌 Project Overview
This project is a Multilingual Text-to-Speech (TTS) API built using Hugging Face MMS models. It converts text input into speech (audio) in multiple languages such as English, Hindi, and Kannada.

🚀 Features
Supports multiple languages
Converts text into speech
FastAPI REST API
Dockerized deployment
Model caching


🛠️ Tech Stack
Python, FastAPI, Uvicorn, Transformers, Torch, SoundFile, Docker

📂 Project Structure
tts-project/
api.py
main.py
tts.py
Dockerfile
requirements.txt
output.wav


⚙️ Installation
pip install -r requirements.txt
python -m uvicorn api:app --host 0.0.0.0 --port 8000

🌐 API Usage
GET /tts?language=kannada&text=ನಮಸ್ಕಾರ

🐳 Docker Setup
docker build -t tts-api .
docker run -p 8000:8000 tts-api


🎧 Output
Audio file will be generated as:
output_<language>.wav


🏁 Conclusion

This project demonstrates ML integration, API development, Docker usage, and DevOps workflow.
