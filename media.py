import webbrowser


class Movie():
    """ This calss defines a movie object and displays movies in a browser """

    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]

    def __init__(self, movie_title, mpaa_rating, movie_story_line, poster_image, trailer_youtube):
        self.title = movie_title
        self.movie_story_line = movie_story_line
        self.mpaa_rating = mpaa_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
