# Import external file dependencies
import Video
import Movie
import fresh_tomatoes

# Movie objects
lordOfTheRings = Movie.Movie("The Lord of the Rings: The Fellowship of the Ring",
							 "Frodo and the Fellowship of the Ring commence their epic journey to deliver the one Ring to its forging ground.",
							 "https://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg",
							 "https://www.youtube.com/watch?v=V75dMMIW2B4",
							 "2:58")


napoleonDynamite = Movie.Movie("Napoleon Dynamite",
							   "The most random movie I've ever seen.",
							   "https://upload.wikimedia.org/wikipedia/en/8/87/Napoleon_dynamite_post.jpg",
							   "https://www.youtube.com/watch?v=ZHDi_AnqwN4",
							   "1:36")

theLegoMovie = Movie.Movie("The Lego Movie",
						   "Fast-moving scenes, lots of crazy LEGO creations, and saving the world - LEGO style. ;)",
						   "https://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg",
						   "https://www.youtube.com/watch?v=fZ_JOBCLF-I",
						   "1:40")

montyPython = Movie.Movie("Monty Python",
						  "The namesake of the Python Programming Language.",
						  "http://upload.wikimedia.org/wikipedia/en/4/49/Monty_python_and_the_holy_grail_2001_release_movie_poster.jpg",
						  "https://www.youtube.com/watch?v=urRkGvhXc8w",
						  "1:31")

theHobbitBOTFA = Movie.Movie("The Hobbit: The Battle of the Five Armies",
							 "The final film in The Hobbit Series.",
							 "http://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",
							 "https://www.youtube.com/watch?v=iVAgTiBrrDA",
							 "2:24")


# Movies array
movies = [lordOfTheRings, napoleonDynamite, theLegoMovie, montyPython, theHobbitBOTFA]

# Open the web site page in default browser
fresh_tomatoes.open_movies_page(movies)