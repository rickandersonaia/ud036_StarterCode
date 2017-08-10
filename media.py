import webbrowser


class Movie():
    """ This class defines a movie object and displays movies in a browser

    def __init__() takes 6 parameters
        self -
        movie_title - the title of the movie - what?!
    Blah, blah, blah, all the rest of this documentation is redundant because
    the code is self documenting.  More documentation than the first line
    simply makes the code less maintainable.

    So, I know I'm just a student but the amount of documentation suggested by
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    is absurd given that you understand how classes work and all of the
    variable and method names are descriptive.

    I still stand by my original as the best level of documentation"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]

    def __init__(self, movie_title, mpaa_rating, movie_story_line,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.movie_story_line = movie_story_line
        self.mpaa_rating = mpaa_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
