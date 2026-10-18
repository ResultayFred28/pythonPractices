class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")

ilangKanta = int(input("enter how many songs you wanna add: "))

for _ in range(ilangKanta):
  kanta = input("add the song: ")
  my_playlist.add_song(kanta)

my_playlist.show_songs()