# Import external file dependencies
from Video import Video
import webbrowser

class Movie(Video):

	"""This class provides a way to store movie related information."""

	# Array of valid movie ratings
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movieTitle, movieStoryline, moviePosterImage, movieTrailerYouTubeURL, duration):

		Video.__init__(self, movieTitle, duration)
		self.title = movieTitle
		self.storyline = movieStoryline
		self.poster_image_url = moviePosterImage
		self.trailer_youtube_url = movieTrailerYouTubeURL
		self.duration = duration

	# Open a browser at location of the movie's YouTube page
	def showTrailer(self):
		webbrowser.open(self.trailer_youtube_url)