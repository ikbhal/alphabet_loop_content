from gtts import gTTS
import os

# Tamil alphabets
alphabets_tamil = "அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ ஃ க ங ச ஜ ஞ ட ண த ந ப ம ய ர ல வ ழ ள ற ன"

output_folder_tamil = "audio/tamil"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_tamil, exist_ok=True)

for alphabet in alphabets_tamil.split():
    tts = gTTS(alphabet, lang='ta')
    file_name = f"{alphabet}.mp3"
    file_path = os.path.join(output_folder_tamil, file_name)
    tts.save(file_path)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_path}")
