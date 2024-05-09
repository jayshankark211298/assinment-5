""" Digital Music Player: A Python program to manage audio files and playlists, 
allowing users to create, search, and rate them"""

import random

class Audio:
#A class representing an audio file
    def __init__(self, name, url):
#Initialize an audio file with a name, URL, and default rating
        self.name = name
        self.url = url
# Default rating is set to 0
        self.rating = 0  
    def set_rating(self, rating):
#Set the rating for the audio file
        self.rating = rating

class Playlist:
#A class representing a playlist
    def __init__(self, name, genre):
#Initialize a playlist with a name, genre, empty list of audios, and default rating
        self.name = name
        self.genre = genre
        self.audios = []  
        self.rating = 0  

    def add_audio(self, audio):
#Add an audio file to the playlist
        self.audios.append(audio)

    def set_rating(self, rating):
#Set the rating for the playlist
        self.rating = rating

class MusicPlayer:
#A class representing a music player
    def __init__(self):
#Initialize a music player with empty lists for audio files and playlists.
        self.audios = []  # List to store all audio files
        self.playlists = []  # List to store all playlists

    def create_audio(self, name, url):
#Create a new audio file and add it to the music player
        audio = Audio(name, url)
        self.audios.append(audio)
        return audio

    def create_playlist(self, name, genre):
#Create a new playlist and add it to the music player
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def add_audio_to_playlist(self, audio, playlist):
#Add an audio file to a playlist.
        playlist.add_audio(audio)

    def search_audio_by_name(self, name):
#Search for audio files by name
        return [audio for audio in self.audios if name.lower() in audio.name.lower()]

    def search_playlist_by_name(self, name):
#Search for playlists by name
        return [playlist for playlist in self.playlists if name.lower() in playlist.name.lower()]

    def calculate_average_rating(self, ratings):
#Calculate the average rating from a list of ratings
        return sum(ratings) / len(ratings)

# Generating random ratings for playlists and audio files
random.seed(42)  # Set the random seed for reproducibility
users = ['User1', 'User2', 'User3']  # Simulating three users
music_player = MusicPlayer()  # Create a new music player object
for _ in range(10):  # Generate 10 audio files and playlists
    audio = music_player.create_audio(f'Audio{_}', f'url{_}')  # Create a new audio file
    playlist = music_player.create_playlist(f'Playlist{_}', f'Genre{_}')  # Create a new playlist
    for user in users:
        # Generate a random rating between 1 and 5 for each audio file and playlist
        rating = random.randint(1, 5)
        audio.set_rating(rating)  # Set the rating for the audio file
        playlist.set_rating(rating)  # Set the rating for the playlist

# Displaying average ratings
playlist_ratings = [playlist.rating for playlist in music_player.playlists]  # Get all playlist ratings
audio_ratings = [audio.rating for audio in music_player.audios]  # Get all audio file ratings

# Calculate the average ratings for playlists and audio files
average_playlist_rating = music_player.calculate_average_rating(playlist_ratings)
average_audio_rating = music_player.calculate_average_rating(audio_ratings)

print("Average Playlist Rating:", average_playlist_rating)  # Display the average playlist rating
print("Average Audio Rating:", average_audio_rating)  # Display the average audio file rating
