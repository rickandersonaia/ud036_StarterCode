import webbrowser

class Movie():
    """ This calss displays movies """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_story_line, poster_image, trailer_youtube):
        self.movie_title = movie_title
        self.movie_story_line = movie_story_line
        self.poster_image = poster_image
        self.trailer_youtube = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
