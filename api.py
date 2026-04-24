from fastapi import FastAPI
from transformers import VitsModel, AutoTokenizer
import torch
import soundfile as sf

app = FastAPI()

language_models = {
    "english": "facebook/mms-tts-eng",
    "hindi": "facebook/mms-tts-hin",
    "kannada": "facebook/mms-tts-kan"
}

# cache models (IMPORTANT for speed)
models = {}
tokenizers = {}

def load_model(lang):
    model_id = language_models[lang]
    if lang not in models:
        models[lang] = VitsModel.from_pretrained(model_id)
        tokenizers[lang] = AutoTokenizer.from_pretrained(model_id)
    return models[lang], tokenizers[lang]

@app.get("/")
def home():
    return {"message": "TTS API is running"}

@app.get("/tts")
def generate_tts(language: str, text: str):
    if language not in language_models:
        return {"error": "Unsupported language"}

    model, tokenizer = load_model(language)

    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = model(**inputs).waveform

    filename = f"output_{language}.wav"
    sf.write(filename, output.squeeze().numpy(), 16000)

    return {"message": "Audio generated", "file": filename}