from gtts import gTTS
import os

# Urdu alphabets
alphabets_urdu = "ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن ں و ہ ھ ء ی ے"

output_folder_urdu = "audio/urdu"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_urdu, exist_ok=True)

for alphabet in alphabets_urdu.split():
    tts = gTTS(alphabet, lang='ur')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_urdu, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
