"""
entertainment center module which creates list of movies objects and hand over
to open_movies_page() funtion in fresh_tomatoes module.
"""
import media
import get_movies_detail
from fresh_tomatoes import open_movies_page


def main():
    # movies = [media.Movie('X-Men: Apocalypse',
    #                       'http://heroichollywood.com/wp-content/uploads/2016/04/maxresdefault-2.jpg',  # noqa
    #                       'https://www.youtube.com/watch?v=N0io2w_6vT8')]

    movie_titles = ['X-Men: Apocalypse']
    movies = []

    for movie_title in movie_titles:
        movie_id = get_movies_detail.get_movie_id(movie_title)
        print('id:{}'.format(movie_id))
        movie_data = get_movies_detail.get_movie_details(movie_id)

        media.Movie(movie_data['title'],
                    movie_data['poster'],
                    movie_data['trailer'])

    # pass list of movies to be displayed in the webpage
    open_movies_page(movies)


if __name__ == '__main__':
    main()
