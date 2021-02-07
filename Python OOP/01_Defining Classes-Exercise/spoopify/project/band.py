class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album.name in map(lambda a: a.name, self.albums):
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        album_names = [a.name for a in self.albums]
        if album_name not in album_names:
            return f'Album {album_name} is not found.'

        album = self.albums[album_names.index(album_name)]
        if album.published:
            return f'Album has been published. It cannot be removed.'

        self.albums.remove(album)
        return f'Album {album_name} has been removed.'

    def details(self):
        return '\n'.join([
            f'Band {self.name}'

        ] + [
            a.details() for a in self.albums
        ]) + '\n'
