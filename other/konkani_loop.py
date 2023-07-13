from gtts import gTTS
import os

# Konkani alphabets
alphabets_konkani = "अ आ इ ई उ ऊ ऋ ए ऐ ओ औ अं अः क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह"

output_folder_konkani = "audio/konkani"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_konkani, exist_ok=True)

for alphabet in alphabets_konkani.split():
    tts = gTTS(alphabet, lang='kok')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_konkani, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
