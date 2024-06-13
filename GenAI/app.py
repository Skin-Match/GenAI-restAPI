from flask import Flask, jsonify, request, json
import base64
import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models
from google.auth import default as default
import os

app = Flask(__name__)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../credentials/GenAIkey.json"


def generate(skin_type, skin_concerns, current_skincare):   
    # Mengatur proyek dan lokasi
    project_id = "cc-c241-ps246"
    location = "us-central1"

    # Inisialisasi kredensial
    credentials, project = default()
    vertexai.init(project=project_id, location=location, credentials=credentials)

    # Inisialisasi model generatif
    model = GenerativeModel(
        "gemini-1.5-flash-001",
    )
    
    # Konfigurasi generasi teks
    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 0.1,
        "top_p": 0.95,
    }
    
    # Pengaturan keamanan
    safety_settings = {
        generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }

    # Membuat prompt berdasarkan input pengguna
    text1 = f"""You are a beauty consultant. Given user skin type, please give recommendation about their skincare routine, what should they do and what shouldn't
    {{
    skin type: {skin_type},
    skin concerns: {skin_concerns},
    current skincare: {current_skincare};
    }}"""

    # Memanggil model untuk menghasilkan konten
    responses = model.generate_content(
        [text1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    # Menangani dan mencetak respons dari model
    result = ""
    for response in responses:
        result += response.text
    return result

@app.route('/')
def home():
    return "Hello, this is your Flask app running in Docker on GCP Cloud Shell!"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            skin_type = data['skin_type']
            skin_concerns = data['skin_concerns']
            current_skincare = data['current_skincare']
            result = generate(skin_type, skin_concerns, current_skincare)
            return jsonify({'result': result})
        else:
            return jsonify({"error": "Unsupported Media Type, please send JSON"}), 415
    else:
        return "Send a POST request with JSON data to this endpoint."

if __name__ == '__main__':
    app.run(debug=True)
