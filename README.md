
## Introduction

Movie Trailer Website is my first project from **Full Stack Web Developer Nanodegree** program. It focuses on
writing server-side code to store a list of your favorite movies, including box art imagery and a movie trailer URL. It generate a static web page allowing visitors to browse their movies and watch the trailers.


## Requirements

* python >= 2.7
* web browser: any recent stable release of Safari/Chrome/Firefox


## Usage

Run `entertainment_center.py`:

* `python <path>/entertainment_center.py`

## Details

* `entertainment_center.py` module creates list of movie objects and passes this list to `open_movies_page()` function.
* `open_movies_page()` generates static webpage with movie title, poster images and youtube url for each movie in the list.
* Movie class defined in `media.py` module and contains only one constructor which creates and initialize movie object with title, poster image url and trailer youtube url.
*  user can click on movie poster image to see it's youtube trailer.


## License

You are allowed to copy, modify and redistribute this project.
