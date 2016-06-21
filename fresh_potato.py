import webbrowser
import os
import re

movie_detail = '''
<div class="col-md-4">
    <img src="{movie_poster_url}" data-toggle="modal" data-target="#{modal_id}" class="img-responsive center-block img-thumbnail" alt="Responsive image">
    <h4>{movie_title}</h4>
</div>
'''

movie_row = '''
<div class="row text-center">
    {row_sep}
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
'''

row_seperator = '''
<div class="row">
    <div class="col-md-12">
        <hr>
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

page_body = '''
<body>
    <div class="container">
        {row1}
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

modal = '''
<!-- Modal -->
<div class="modal fade" id="{modal_id}" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
<div class="modal-dialog" role="document">
<div class="modal-content">
    <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="myModalLabel">{movie_title}</h4>
    </div>
    <div class="modal-body">
        ...
    </div>
    <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
    </div>
</div>
</div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    rows = ''
    movies_tuples = [movies[i:i+3] for i in range(0, len(movies), 3)]
    module_no = 0
    for movie_tuple in movies_tuples:
        row_data = ''
        for movie in movie_tuple:
            module_no += 1
            row_data += movie_detail.format(movie_poster_url=movie.poster_image_url,
                                            movie_title=movie.title,
                                            modal_id='modal_{}'.format(module_no))

        rows += movie_row.format(row_sep=row_seperator, movies=row_data)

    return rows


def create_movie_modals(movies):
    modals = ''
    for index, movie in enumerate(movies):
        modals += modal.format(modal_id='modal_{}'.format(index), movie_title=movie.title)

    return modals


def open_movies_page(movies):
    # Create or overwrite the output file
    try:
        output_file = open('fresh_potato.html', 'w')
    except Exception as e:
        print(e)

    modals = create_movie_modals(movies)

    body = page_body.format(row1=first_row,
                            mov_rows=create_movie_tiles_content(movies),
                            modals=modals)

    html_page = page.format(head=head, body=body)

    # Output the file
    output_file.write(html_page)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
