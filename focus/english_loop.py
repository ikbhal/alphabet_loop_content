import pygame
import os

def play_all_audio_files(folder_path):
    # Initialize pygame
    pygame.mixer.init()

    # Get the list of files in the folder
    files = os.listdir(folder_path)

    for file in files:
        # Check if the file is an MP3 file
        if file.endswith('.mp3'):
            # Construct the file path
            file_path = os.path.join(folder_path, file)

            # Load and play the audio file
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

            # Wait for the audio to finish playing
            while pygame.mixer.music.get_busy():
                continue

    # Clean up
    pygame.mixer.quit()

def play_specific_audio_files(audio_list, folder_path):
    # Initialize pygame
    pygame.mixer.init()

    for audio in audio_list:
        # Construct the file path
        file_path = os.path.join(folder_path, audio + '.mp3')

        # Load and play the audio file
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            continue

    # Clean up
    pygame.mixer.quit()

# Example usage
audio_folder_path = 'audio'

# Play all audio files in the folder
# play_all_audio_files(audio_folder_path)

# Play specific audio files based on a list
specific_audio_list = ['a', 'b', 'c']

while True:
    play_specific_audio_files(specific_audio_list, audio_folder_path)
