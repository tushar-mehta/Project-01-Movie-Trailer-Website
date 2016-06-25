import webbrowser
import os
import re

movie_detail = '''
<div class="col-md-4">
    <img width="220" height="340" src="{poster_image_url}" data-toggle="modal" data-target="#{modal_id}" class="img-responsive center-block img-thumbnail" alt="Responsive image">
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
            <p><b>Director: </b>{director}</p>
            <p><b>Rating: </b>{rating}</p>
            <p><b>Duration: </b>{duration}</p>
            <p><b>Genre: </b>{genre}</p>
        </div>

        <div class="modal-footer">
            <a class="btn btn-default" href="{trailer_youtube_url}" role="button" data-width="800" data-height="420">YouTube Trailer</a>
        </div>
</div>

</div>
</div>
</div>
'''

video_generic_modal = '''
<!-- Video / Generic Modal -->
<div class="modal fade" id="mediaModal" tabindex="-1" role="dialog" aria-hidden="true">
<div class="modal-dialog">
    <div class="modal-content">
        <div class="modal-body">
            <!-- content dynamically inserted -->
        </div>
    </div>
</div>
</div>
'''

script = '''
// REQUIRED: "jQuery Query Parser" plugin.
// https://github.com/mattsnider/jquery-plugin-query-parser
// Minified version here:
 (function($){var pl=/\+/g,searchStrict=/([^&=]+)=+([^&]*)/g,searchTolerant=/([^&=]+)=?([^&]*)/g,decode=function(s){return decodeURIComponent(s.replace(pl," "));};$.parseQuery=function(query,options){var match,o={},opts=options||{},search=opts.tolerant?searchTolerant:searchStrict;if('?'===query.substring(0,1)){query=query.substring(1);}while(match=search.exec(query)){o[decode(match[1])]=decode(match[2]);}return o;};$.getQuery=function(options){return $.parseQuery(window.location.search,options);};$.fn.parseQuery=function(options){return $.parseQuery($(this).serialize(),options);};}(jQuery));

// YOUTUBE VIDEO CODE
$(document).ready(function(){

// BOOTSTRAP 3.0 - Open YouTube Video Dynamicaly in Modal Window
// Modal Window for dynamically opening videos
$('a[href^="http://www.youtube.com"]').on('click', function(e){
  // Store the query string variables and values
	// Uses "jQuery Query Parser" plugin, to allow for various URL formats (could have extra parameters)
	var queryString = $(this).attr('href').slice( $(this).attr('href').indexOf('?') + 1);
	var queryVars = $.parseQuery( queryString );

	// if GET variable "v" exists. This is the Youtube Video ID
	if ( 'v' in queryVars )
	{
		// Prevent opening of external page
		e.preventDefault();

		// Variables for iFrame code. Width and height from data attributes, else use default.
		var vidWidth = 560; // default
		var vidHeight = 315; // default
		if ( $(this).attr('data-width') ) { vidWidth = parseInt($(this).attr('data-width')); }
		if ( $(this).attr('data-height') ) { vidHeight =  parseInt($(this).attr('data-height')); }
		var iFrameCode = '<iframe width="' + vidWidth + '" height="'+ vidHeight +'" scrolling="no" allowtransparency="true" allowfullscreen="true" src="http://www.youtube.com/embed/'+  queryVars['v'] +'?rel=0&wmode=transparent&showinfo=0" frameborder="0"></iframe>';

		// Replace Modal HTML with iFrame Embed
		$('#mediaModal .modal-body').html(iFrameCode);
		// Set new width of modal window, based on dynamic video content
		$('#mediaModal').on('show.bs.modal', function () {
			// Add video width to left and right padding, to get new width of modal window
			var modalBody = $(this).find('.modal-body');
			var modalDialog = $(this).find('.modal-dialog');
			var newModalWidth = vidWidth + parseInt(modalBody.css("padding-left")) + parseInt(modalBody.css("padding-right"));
			newModalWidth += parseInt(modalDialog.css("padding-left")) + parseInt(modalDialog.css("padding-right"));
			newModalWidth += 'px';
			// Set width of modal (Bootstrap 3.0)
		    $(this).find('.modal-dialog').css('width', newModalWidth);
		});

		// Open Modal
		$('#mediaModal').modal();
	}
});

// Clear modal contents on close.
// There was mention of videos that kept playing in the background.
$('#mediaModal').on('hidden.bs.modal', function () {
	$('#mediaModal .modal-body').html('');
});

});
'''

head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Patato!</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
</head>
'''

body = '''
<body>
    <div class="container">
        {nav}
        {mov_rows}
    </div>
    {modals}
    {video_generic_modal}
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script>{script}</script>
</body>
'''

page = '''
<!DOCTYPE html>
<html lang="en">
{head}
{body}
</html>
'''

movie_row = '''
<div class="row">
{movie0}
{movie1}
{movie2}
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    cols = []
    for index, movie in enumerate(movies):
        cols.append(movie_detail.format(poster_image_url=movie.poster_image_url,
                                    movie_title=movie.title,
                                    modal_id='modal_{}'.format(index)))

    while len(cols) % 3 != 0:
        cols.append('')

    it = iter(cols)
    col_tuples = zip(it, it, it)

    rows = ''

    for col0, col1, col2 in col_tuples:
        rows += movie_row.format(movie0=col0,
                                 movie1=col1,
                                 movie2=col2)

    return rows


def create_movie_modals(movies):
    modals = ''
    for index, movie in enumerate(movies):
        modals += modal.format(modal_id='modal_{}'.format(index),
                               movie_title=movie.title,
                               movie_synopsis=movie.movie_synopsis,
                               trailer_youtube_url=movie.trailer_youtube_url,
                               director=movie.director,
                               rating=movie.rating,
                               duration=movie.duration,
                               genre=movie.genre)

    return modals


def open_movies_page(movies):
    # Create or overwrite the output file
    try:
        output_file = open('fresh_potato.html', 'w')
    except Exception as e:
        print(e)

    page_body = body.format(nav=nav,
                            mov_rows=create_movie_tiles_content(movies),
                            modals=create_movie_modals(movies),
                            video_generic_modal=video_generic_modal,
                            script=script)

    html_page = page.format(head=head, body=page_body)

    # Output the file
    output_file.write(html_page)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
