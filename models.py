class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def like_it(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f'Name: {self.name} Likes: {self.likes}'


class Movie(Program):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length

    def __str__(self):
        return f'Name: {self.name} - {self.length} min - Likes: {self.likes}'


class Series(Program):
    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season

    def __str__(self):
        return f'Name: {self.name} - {self.season} season(s) - Likes: {self.likes}'


class Playlist():
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    @property
    def listing(self):
        return self._programs

    @property
    def size(self):
        return len(self._programs)


gump = Movie('Forrest Gump', 1994, 142)
redenmption = Movie('The Shawshank Redemption', 1994, 142)
tbbt = Series('The Big Bang Theory', 2007, 12)
got = Series('Game of Thrones', 2011, 8)

gump.like_it()
gump.like_it()
gump.like_it()
gump.like_it()
redenmption.like_it()
redenmption.like_it()
redenmption.like_it()
tbbt.like_it()
tbbt.like_it()
tbbt.like_it()
tbbt.like_it()
got.like_it()
got.like_it()
got.like_it()

movies_and_series = [tbbt, gump, redenmption, got]

weekeend_playlist = Playlist('Weekend', movies_and_series)

print(f'Playlist size: {weekeend_playlist.size}')

for program in weekeend_playlist:
    print(program)

print(f'Is Forrest Gump in the playslist? {gump in weekeend_playlist}')
