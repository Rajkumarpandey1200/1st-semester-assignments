import pygame

# Initialize pygame
pygame.init()

# Load the audio file (replace 'your_song.mp3' with the actual file path)
song_file = 'E:\python\Aaja_We_Mahiya(256k).mp3'
pygame.mixer.music.load(song_file)

# Play the song
pygame.mixer.music.play()

# Keep the program running until the song ends
while pygame.mixer.music.get_busy():
    continue
