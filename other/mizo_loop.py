from gtts import gTTS
import os

# Mizo alphabets
alphabets_mizo = "ꯀ ꯁ ꯂ ꯃ ꯄ ꯅ ꯆ ꯇ ꯈ ꯉ ꯊ ꯋ ꯌ ꯍ ꯎ ꯏ ꯐ ꯑ ꯒ ꯓ ꯔ ꯕ ꯖ ꯗ ꯘ ꯙ ꯚ ꯛ ꯜ ꯝ ꯞ ꯟ ꯠ ꯡ ꯢ ꯣ ꯤ ꯥ ꯦ ꯧ ꯨ ꯩ ꯪ ꯫ ꯬ ꯭ ꯮ ꯯"

output_folder_mizo = "audio/mizo"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_mizo, exist_ok=True)

for alphabet in alphabets_mizo.split():
    tts = gTTS(alphabet, lang='lus')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_mizo, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
