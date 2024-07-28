import uuid
from datetime import datetime

class Room:
    def __init__(self, name, creator):
        self.id = str(uuid.uuid4())
        self.name = name
        self.creator = creator
        self.users = []
        self.playlists = []
        self.created_at = datetime.now()
        self.current_song = None

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def add_songs_to_playlist(self, playlist):
        if playlist not in self.playlists:
            self.playlists.append(playlist)

    def remove_songs_from_playlist(self, playlist):
        if playlist in self.playlists:
            self.playlists.remove(playlist)

    def play_next_song(self):
        if self.playlists:
            self.current_song = self.playlists.pop(0)
            return self.current_song
        return None
    
    def get_current_song(self):
        return self.current_song
    
