from gtts import gTTS
import os

# Telugu alphabets
alphabets_telugu = "అ ఆ ఇ ఈ ఉ ఊ ఋ ఎ ఏ ఐ ఒ ఓ ఔ అం అః క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ"

output_folder_telugu = "audio/telugu"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_telugu, exist_ok=True)

for alphabet in alphabets_telugu.split():
    tts = gTTS(alphabet, lang='te')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_telugu, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
