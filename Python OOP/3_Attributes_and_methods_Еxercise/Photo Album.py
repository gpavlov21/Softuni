import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(pages=math.ceil(photos_count/4))

    def add_photo(self, label: str):
        for idx, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f'{label} photo added successfully on page {idx+ 1} slot {len(page)}'
        return 'No more free spots'

    def display(self):
        result = []
        for page in self.photos:
            result.append('-'*11)
            result.append(('[] ' * len(page)).rstrip(' '))
        result.append('-' * 11)

        return "\n".join(result) + '\n'


album = PhotoAlbum.from_photos_count(13)
print(album.pages)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("first dsa"))
print(album.add_photo("first EncapsulationExercise"))
print(album.add_photo("first s"))
print(album.add_photo("first d"))

print(album.display())
