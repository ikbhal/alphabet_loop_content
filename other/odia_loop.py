from gtts import gTTS
import os

# Odia alphabets
alphabets_odia = "ଅ ଆ ଇ ଈ ଉ ଊ ଋ ଏ ଐ ଓ ଔ ଅଂ ଅଃ କ ଖ ଗ ଘ ଙ ଚ ଛ ଜ ଝ ଞ ଟ ଠ ଡ ଢ ଣ ତ ଥ ଦ ଧ ନ ପ ଫ ବ ଭ ମ ୟ ର ଲ ଵ ଶ ଷ ସ ହ"

output_folder_odia = "audio/odia"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_odia, exist_ok=True)

for alphabet in alphabets_odia.split():
    tts = gTTS(alphabet, lang='or')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_odia, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
