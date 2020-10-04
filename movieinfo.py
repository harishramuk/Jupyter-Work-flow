class movies:
    '''This movie ditels given by Mr.Harris'''
    def __init__(self,MOVIE,HERO,DIRECTOR):
        self.movie = MOVIE
        self.hero = HERO
        self.director = DIRECTOR
    def take(delf):
        print('Name of the movie:', delf.movie)
        print('Name of the hero:',delf.hero)
        print('Name of the director:',delf.director)
list_info_movie = []
while True:
    MOVIES = input('enter the movie name:')
    HEROS = input('enter the hero name:')
    DIRECTORS = input ('enter the director name:')
    m = movies(MOVIES,HEROS,DIRECTORS)
    list_info_movie.append(m)
    print('movies info uploda success...')
    option = input('if you want add moer movies..[yes/No].')
    if option.lower() == 'no':
        break
for movie in list_info_movie:
    movie.take()
    print()
