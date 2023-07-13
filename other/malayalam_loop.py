from gtts import gTTS
import os

# Malayalam alphabets
alphabets_malayalam = "അ ആ ഇ ഈ ഉ ഊ ഋ എ ഏ ഐ ഒ ഓ ഔ ക ഖ ഗ ഘ ങ ച ഛ ജ ഝ ഞ ട ഠ ഡ ഢ ണ ത ഥ ദ ധ ന പ ഫ ബ ഭ മ യ ര ല വ ശ ഷ സ ഹ"

output_folder_malayalam = "audio/malayalam"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_malayalam, exist_ok=True)

for alphabet in alphabets_malayalam.split():
    tts = gTTS(alphabet, lang='ml')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_malayalam, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
