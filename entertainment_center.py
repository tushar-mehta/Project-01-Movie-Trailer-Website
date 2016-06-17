"""
entertainment center module which creates list of movies objects and hand over
to open_movies_page() funtion in fresh_tomatoes module.
"""
import media
from fresh_tomatoes import open_movies_page


def main():
    movies = [media.Movie('X-Men: Apocalypse',
                          'http://heroichollywood.com/wp-content/uploads/2016/04/maxresdefault-2.jpg',  # noqa
                          'https://www.youtube.com/watch?v=N0io2w_6vT8')]

    # pass list of movies to be displayed in the webpage
    open_movies_page(movies)

if __name__ == '__main__':
    main()
