import webbrowser
import os
import re

movie_detail = '''
<div class="col-md-4">
    <img src="{poster_image_url}" data-toggle="modal" data-target="#{modal_id}" class="img-responsive center-block img-thumbnail" alt="Responsive image">
    <h4 class="text-center">{movie_title}</h4>
</div>
'''

movie_row = '''
<div class="row text-center">
    {row_sep}
    {movies}
</div>
'''

nav = '''
<div class="jumbotron">
<h1>Movie World!</h1>
<p>Browse your favorite movies and watch youtube trailers!</p>
</div>
'''

modal = '''
<!-- Modal -->
<div class="modal fade" id="{modal_id}" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
<div class="modal-dialog" role="document">
<div class="modal-content">
    <!-- Modal content-->
    <div class="modal-content">
        <div class="modal-header">
            <h4 class="modal-title">{movie_title}</h4>
        </div>

        <div class="modal-body">
            <p>{movie_synopsis}</p>
        </div>

        <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">YouTube</button>
        </div>
</div>

</div>
</div>
</div>
'''

head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Patato!</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
</head>
'''

body = '''
<body>
    <div class="container">
        {nav}
        {mov_rows}
        {modals}
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
    for index, movie in enumerate(movies):
        rows += movie_detail.format(poster_image_url=movie.poster_image_url,
                                    movie_title=movie.title,
                                    modal_id='modal_{}'.format(index))
    return rows


def create_movie_modals(movies):
    modals = ''
    for index, movie in enumerate(movies):
        modals += modal.format(modal_id='modal_{}'.format(index),
                               movie_title=movie.title,
                               movie_synopsis=movie.movie_synopsis)

    return modals


def open_movies_page(movies):
    # Create or overwrite the output file
    try:
        output_file = open('fresh_potato.html', 'w')
    except Exception as e:
        print(e)

    page_body = body.format(nav=nav,
                            mov_rows=create_movie_tiles_content(movies),
                            modals=create_movie_modals(movies))

    html_page = page.format(head=head, body=page_body)

    # Output the file
    output_file.write(html_page)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
