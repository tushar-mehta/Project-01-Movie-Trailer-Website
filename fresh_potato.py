import webbrowser
import os
import re

movie_detail = '''
<div class="col-md-4">
    <img src="{movie_poster_url}">
    <h3>{movie_title}</h3>
    <h2>{trailer_youtube_url}</h2>
</div>
'''

movie_row = '''
<div class="row text-center">
    {movies}
</div>
'''

first_row = '''
<div class="row">
    <h1>My Movies</h1>
</div>
<div class="row">
    <h1>Other Information</h1>
</div>
<div class="row">
    <div class="col-md-12">
        <hr>
    </div>
</div>
'''

row_seperator = '''
<div class="row">
    <div class="col-md-12">
        <hr>
    </div>
</div>
'''

page_head = '''
<head>
    <meta charset="utf-8">
    <title>Hello World</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
</head>
'''

page_body = '''
<body>
    <div class="container">
        {row1}
        {mov_rows}
        {row_sep}
    </div>
</body>
'''

page = '''
<!DOCTYPE html>
<html lang="en">
{head}
{body}
</html>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    rows = ''
    movies_tuples = [movies[i:i+3] for i in range(0, len(movies), 3)]
    for movie_tuple in movies_tuples:
        row_data = ''
        for movie in movie_tuple:
            row_data += movie_detail.format(movie_poster_url=movie.poster_image_url,
                                            movie_title=movie.title,
                                            trailer_youtube_url=movie.trailer_youtube_url)

        rows += movie_row.format(movies=row_data)

    return rows


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_potato.html', 'w')

    page_body.format(row1=first_row,
                     mov_rows=create_movie_tiles_content(movies),
                     row_sep=row_seperator)

    page.format(head=page_head, body=page_body)

    # Output the file
    output_file.write(page)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
