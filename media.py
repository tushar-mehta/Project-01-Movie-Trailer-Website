class Movie:
    """
    creates movie object with title, poste image url and trailer youtube url.
    """
    def __init__(self, title, synopsis,
                 poster_image_url,
                 trailer_youtube_url,
                 director,
                 rating,
                 duration,
                 genre):
        self.title = title
        self.synopsis = synopsis
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.director = director
        self.rating = rating
        self.duration = duration
        self.genre = genre
