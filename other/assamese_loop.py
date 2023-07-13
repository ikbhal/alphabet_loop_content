from gtts import gTTS
import os

# Assamese alphabets
alphabets_assamese = "অ আ ই ঈ উ ঊ ঋ এ ঐ ও ঔ অং অঁ ক খ গ ঘ ঙ চ ছ জ ঝ ঞ ট ঠ ড ঢ ণ ত থ দ ধ ন প ফ ব ভ ম য ৰ ল ৱ শ ষ স হ"

output_folder_assamese = "audio/assamese"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_assamese, exist_ok=True)

for alphabet in alphabets_assamese.split():
    tts = gTTS(alphabet, lang='as')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_assamese, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
