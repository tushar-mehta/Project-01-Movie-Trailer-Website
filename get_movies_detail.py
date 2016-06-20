import tmdbsimple as tmdb

tmdb.API_KEY = 'e8a1ed4167cb79da4227bd3844eb94cf'


def get_movie_details(movie_id):
    movie = tmdb.Movies(movie_id).info()

    print(movie)

    movie_dict = {}
    movie_dict['title'] = movie['original_title']
    movie_dict['poster'] = 'http://image.tmdb.org/t/p/w342' + \
        movie['poster_path']

    # videos = movie.videos()['results']
    # for video in videos:
    #     if video['site'] == 'YouTube' and video['type'] == 'Trailer':
    #         movie_dict['trailer'] = 'https://www.youtube.com/watch?v=' + video['key']
    #         break

    return movie_dict


def get_movie_id(movie_title):
    search = tmdb.Search()
    search.movie(query=movie_title)

    # return first movie
    return search.results[0]['id']

    # for s in search.results:
    #     print(s['title'], s['id'], s['release_date'], s['popularity'])
