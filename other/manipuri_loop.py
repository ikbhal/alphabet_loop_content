from gtts import gTTS
import os

# Manipuri alphabets
alphabets_manipuri = "ꯀ ꯁ ꯂ ꯃ ꯄ ꯅ ꯆ ꯇ ꯈ ꯉ ꯊ ꯋ ꯌ ꯍ ꯎ ꯏ ꯐ ꯑ ꯒ ꯓ ꯔ ꯕ ꯖ ꯗ ꯘ ꯙ ꯚ ꯛ ꯜ ꯝ ꯞ ꯟ ꯠ ꯡ ꯢ ꯣ ꯤ ꯥ ꯦ ꯧ ꯨ ꯩ ꯪ ꯫ ꯬ ꯭ ꯮ ꯯"

output_folder_manipuri = "audio/manipuri"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_manipuri, exist_ok=True)

for alphabet in alphabets_manipuri.split():
    tts = gTTS(alphabet, lang='mni')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_manipuri, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
