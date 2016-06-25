"""
entertainment center module which creates list of movies objects and hand over
to open_movies_page() funtion in fresh_tomatoes module.
"""
import media
# from fresh_tomatoes import open_movies_page
from fresh_potato import open_movies_page


def main():
    movies = [media.Movie('Transformers: Age of Extinction',
                          'Autobots must <escape></escape> sight from a bounty hunter who \
                          has taken control of the human serendipity: \
                          Unexpectedly, Optimus Prime and his remaining gang \
                          turn to a mechanic, his daughter, and her back \
                          street racing boyfriend for help.',
                          'http://vignette3.wikia.nocookie.net/transformers/images/9/94/Transformers_Age_of_Extinction_Poster.jpeg/revision/latest?cb=20141123051730',  # noqa
                          'http://www.youtube.com/watch?v=Ru0rnAkekOs',
                          'Michael Bay',
                          'PG-13',
                          '2h 45min',
                          'Action, Adventure, Sci-Fi'),
              media.Movie('Mechanic: Resurrection',
                          'Arthur Bishop thought he had put his murderous past \
                          behind him when his most formidable foe kidnaps the \
                          love of his life. Now he is forced to travel the \
                          globe to complete three impossible assassinations, \
                          and do what he does best, make them look like \
                          accidents.',
                          'http://cdn1-www.comingsoon.net/assets/uploads/gallery/mechanic-resurrection/mechanicposter.jpg',  # noqa
                          'http://www.youtube.com/watch?v=QF903RaKLvs',
                          'Dennis Gansel',
                          'R',
                          '2h 15min',
                          'Action, Crime, Thriller'),
              media.Movie('Finding Dory',
                          'The friendly-but-forgetful blue tang fish reunites \
                          with her loved ones, and everyone learns a few \
                          things about the real meaning of family along \
                          the way.',
                          'http://vignette4.wikia.nocookie.net/pixar/images/0/0e/FINDING_DORY_-_Key_Art.jpg/revision/latest?cb=20160515234044',  # noqa
                          'http://www.youtube.com/watch?v=pSf-5vbVpAU',
                          'Andrew Stanton, Angus MacLane',
                          'PG',
                          '1h 43min',
                          'Animation, Adventure, Comedy'),
              media.Movie('Finding Dory',
                          'The friendly-but-forgetful blue tang fish reunites \
                          with her loved ones, and everyone learns a few \
                          things about the real meaning of family along \
                          the way.',
                          'http://vignette4.wikia.nocookie.net/pixar/images/0/0e/FINDING_DORY_-_Key_Art.jpg/revision/latest?cb=20160515234044',  # noqa
                          'http://www.youtube.com/watch?v=pSf-5vbVpAU',
                          'Andrew Stanton, Angus MacLane',
                          'PG',
                          '1h 43min',
                          'Animation, Adventure, Comedy'),
             media.Movie('Finding Dory',
                         'The friendly-but-forgetful blue tang fish reunites \
                         with her loved ones, and everyone learns a few \
                         things about the real meaning of family along \
                         the way.',
                         'http://vignette4.wikia.nocookie.net/pixar/images/0/0e/FINDING_DORY_-_Key_Art.jpg/revision/latest?cb=20160515234044',  # noqa
                         'http://www.youtube.com/watch?v=pSf-5vbVpAU',
                         'Andrew Stanton, Angus MacLane',
                         'PG',
                         '1h 43min',
                         'Animation, Adventure, Comedy'),
              media.Movie('Finding Dory',
                          'The friendly-but-forgetful blue tang fish reunites \
                          with her loved ones, and everyone learns a few \
                          things about the real meaning of family along \
                          the way.',
                          'http://vignette4.wikia.nocookie.net/pixar/images/0/0e/FINDING_DORY_-_Key_Art.jpg/revision/latest?cb=20160515234044',  # noqa
                          'http://www.youtube.com/watch?v=pSf-5vbVpAU',
                          'Andrew Stanton, Angus MacLane',
                          'PG',
                          '1h 43min',
                          'Animation, Adventure, Comedy')

            ]

    # pass list of movies to be displayed in the webpage
    open_movies_page(movies)

if __name__ == '__main__':
    main()
