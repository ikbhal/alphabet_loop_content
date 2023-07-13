from gtts import gTTS
import os

# Kannada alphabets
alphabets_kannada = "ಅ ಆ ಇ ಈ ಉ ಊ ಋ ಎ ಏ ಐ ಒ ಓ ಔ ಅಂ ಅಃ ಕ ಖ ಗ ಘ ಙ ಚ ಛ ಜ ಝ ಞ ಟ ಠ ಡ ಢ ಣ ತ ಥ ದ ಧ ನ ಪ ಫ ಬ ಭ ಮ ಯ ರ ಲ ವ ಶ ಷ ಸ ಹ"

output_folder_kannada = "audio/kannada"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_kannada, exist_ok=True)

for alphabet in alphabets_kannada.split():
    tts = gTTS(alphabet, lang='kn')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_kannada, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
