from gtts import gTTS
import os

# Gujarati alphabets
alphabets_gujarati = "અ આ ઇ ઈ ઉ ઊ ઋ એ ઐ ઓ ઔ અં અઃ ક ખ ગ ઘ ઙ ચ છ જ ઝ ઞ ટ ઠ ડ ઢ ણ ત થ દ ધ ન પ ફ બ ભ મ ય ર લ વ શ ષ સ હ"

output_folder_gujarati = "audio/gujarati"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_gujarati, exist_ok=True)

for alphabet in alphabets_gujarati.split():
    tts = gTTS(alphabet, lang='gu')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_gujarati, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
