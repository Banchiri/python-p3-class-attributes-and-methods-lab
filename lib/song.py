class Song:
    count = 0
    GENRES = []
    ARTISTS = []
    genre_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count(self)
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
    @classmethod
    def add_to_genres(cls, genre):
        cls.GENRES.append(genre)
    @classmethod
    def add_to_artists(cls, artist):
        cls.ARTISTS.append(artist)
    @classmethod
    def add_to_genre_count(cls,genre):
        if genre in cls.genre_count:
            #increment if genre ALREADY exists
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    



    
