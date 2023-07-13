import pygame

# Initialize pygame
pygame.mixer.init()

# Load the audio file
# audio_file = "path_to_audio_file.mp3"
audio_file = "audio/a.mp3"
pygame.mixer.music.load(audio_file)

# Play the audio file
pygame.mixer.music.play()

# Wait for the audio to finish playing
while pygame.mixer.music.get_busy():
    continue

# Clean up
pygame.mixer.quit()
