from gtts import gTTS

# English alphabets
alphabets = "abcdefghijklmnopqrstuvwxyz"

for alphabet in alphabets:
    tts = gTTS(alphabet, lang='en')
    file_name = f"{alphabet}.mp3"
    tts.save(file_name)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_name}")
