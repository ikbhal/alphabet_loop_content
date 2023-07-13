from gtts import gTTS
import os

# Bengali alphabets
alphabets_bengali = "অ আ ই ঈ উ ঊ ঋ এ ঐ ও ঔ ং ঃ ক খ গ ঘ ঙ চ ছ জ ঝ ঞ ট ঠ ড ঢ ণ ত থ দ ধ ন প ফ ব ভ ম য র ল শ ষ স হ ড় ঢ় য়"

output_folder_bengali = "audio/bengali"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_bengali, exist_ok=True)

for alphabet in alphabets_bengali.split():
    tts = gTTS(alphabet, lang='bn')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_bengali, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
