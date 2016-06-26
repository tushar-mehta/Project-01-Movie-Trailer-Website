"""
entertainment center module which creates list of movies objects and hand over
to open_movies_page() funtion in fresh_tomatoes module.
"""
import sys
import json
import media
# from fresh_tomatoes import open_movies_page
from fresh_potato import open_movies_page
from fresh_potato import open_error_page

movie_html_page_name = 'fresh_potato.html'
error_html_page = 'error.html'


def main():
    json_data = ''
    try:
        with open('movies.json') as jsonfile:
            json_data = json.load(jsonfile)
    except Exception as e:
        open_error_page(error_html_page, 'Failed to load movies!')
        sys.exit(-1)

    movies = []
    for movie_json in json_data:
        movies.append(media.Movie(movie_json['title'],
                                  movie_json['synopsis'],
                                  movie_json['poster_image_url'],
                                  movie_json['trailer_youtube_url'],
                                  movie_json['director'],
                                  movie_json['rating'],
                                  movie_json['duration'],
                                  movie_json['genre']))

    # pass list of movies to be displayed in the webpage
    open_movies_page(movie_html_page_name, movies)

if __name__ == '__main__':
    main()
