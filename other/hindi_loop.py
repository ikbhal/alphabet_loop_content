from gtts import gTTS

# Hindi alphabets
alphabets = "अ आ इ ई उ ऊ ऋ ए ऐ ओ औ अं अः क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह"

for alphabet in alphabets.split():
    tts = gTTS(alphabet, lang='hi')
    file_name = f"{alphabet}.mp3"
    tts.save(file_name)
    print(f"Generated audio file for alphabet {alphabet} and saved as {file_name}")
