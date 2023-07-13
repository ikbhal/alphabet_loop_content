from flask import Flask, send_file, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

audio_folder = "../audio"

@app.route('/audio/<lang>/<alphabet>')
def get_audio(lang, alphabet):
    # Validate the language and alphabet
    lang = lang.lower()
    alphabet = alphabet.lower()

    # Construct the file path
    file_path = os.path.join(audio_folder, lang, f"{alphabet}.mp3")

    # Check if the file exists
    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return "Audio file not found", 404

print("before main")

if __name__ == '__main__':
    print("inside main")
    app.run()
