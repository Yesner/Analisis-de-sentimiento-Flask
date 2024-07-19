# app.py

from flask import Flask, request, render_template, jsonify
import pandas as pd
import os
from functions import find_sentiment, extract_entities, process_audio

app = Flask(__name__)

# Directorio para guardar archivos de audio
AUDIO_FOLDER = "./audio_files"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process_audio', methods=['POST'])
def process_audio_route():
    if 'audio_file' in request.files:
        audio_file = request.files['audio_file']
        audio_path = os.path.join(AUDIO_FOLDER, secure_filename(audio_file.filename))
        audio_file.save(audio_path)
        text = process_audio(audio_path)
        return jsonify({"transcription": text})

@app.route('/process-transcriptions', methods=['POST'])
def process_transcriptions():
    # La lógica para procesar transcripciones permanece aquí
    # Utiliza find_sentiment y extract_entities según sea necesario

if __name__ == '__main__':
    app.run(debug=True)