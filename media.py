import webbrowser
class Movie():
    """Initial function"""
    def __init__ (self,movie_title,movie_storyline,poster_image,
                  trailer_youtube,director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director_name = director
    """ function to show the trailer using the link."""    
    def show_trailer():
        webbrowser.open(self.trailer_youtube_url)
