class Movie:
    """
    creates movie object with title, poste image url and trailer youtube url.
    """
    def __init__(self, title, movie_synopsis, poster_image_url, trailer_youtube_url):
        self.title = title
        self.movie_synopsis = movie_synopsis
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
