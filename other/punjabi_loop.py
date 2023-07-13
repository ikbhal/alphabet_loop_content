# // language not supported by gTTS, so we have to use the language code

from gtts import gTTS
import os

# Punjabi alphabets
alphabets_punjabi = "ਅ ਆ ਇ ਈ ਉ ਊ ਏ ਐ ਓ ਔ ੲ ਕ ਖ ਗ ਘ ਙ ਚ ਛ ਜ ਝ ਞ ਟ ਠ ਡ ਢ ਣ ਤ ਥ ਦ ਧ ਨ ਪ ਫ ਬ ਭ ਮ ਯ ਰ ਲ ਵ ੜ ਸ਼ ਸ ਹ ਲ਼"

output_folder_punjabi = "audio/punjabi"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_punjabi, exist_ok=True)

for alphabet in alphabets_punjabi.split():
    tts = gTTS(alphabet, lang='pa')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_punjabi, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
