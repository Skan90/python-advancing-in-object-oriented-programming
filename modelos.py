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


class Filme(Program):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length
    
    def __str__(self):
        return f'Name: {self.name} - {self.length} min - Likes: {self.likes}'


class Serie(Program):
    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season

    def __str__(self):
        return f'Name: {self.name} - {self.season} season(s) - Likes: {self.likes}'


gump = Filme('Forrest Gump', 1994, 142)
tbbt = Serie('The Big Bang Theory', 2007, 12)
gump.like_it()
gump.like_it()
gump.like_it()

tbbt.like_it()
tbbt.like_it()

listing = [tbbt, gump]

for program in listing:
    print(program)
