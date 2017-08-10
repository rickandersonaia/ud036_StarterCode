import fresh_tomatoes
import media


unforgiven = media.Movie(
    "Unforgiven",
    "A whippin'? That's all they get after all they done?",
    "R",
    "https://s-media-cache-ak0.pinimg.com/originals/c5/d6/3d/c5d63dace25bb3554c9ed1c2eb45a806.jpg",  # noqa
    "https://www.youtube.com/watch?v=XDAXGILEdro")

big_lebowski = media.Movie(
    "The Big Lebowski",
    "That rug really tied the room together, man",
    "R",
    "http://img.moviepostershop.com/the-big-lebowski-movie-poster-1998-1020196337.jpg",  # noqa
    "https://www.youtube.com/watch?v=cd-go0oBF4Y")

pulp_fiction = media.Movie(
    "Pulp Fiction",
    "Check out the big brain on Brad!",
    "R",
    "https://moviefiles.alphacoders.com/777/poster-thumb-77.jpg",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

true_romance = media.Movie(
    "True Romance",
    "Love conquers all",
    "R",
    "https://s-media-cache-ak0.pinimg.com/originals/20/96/52/2096528e05bee04ab065f27446b242cc.jpg",  # noqa
    "https://www.youtube.com/watch?v=0AIbZDBC8tk")

team_america = media.Movie(
    "Team America World Police",
    "Freedom isn't free.  It's gotta hefty fuckin fee",
    "R",
    "http://www.impawards.com/2004/posters/team_america_world_police_ver2.jpg",
    "https://www.youtube.com/watch?v=RPBX47zSktc")

guffman = media.Movie(
    "Waiting for Guffman",
    "A community theatre waits for a New York Times reviewer",
    "R",
    "http://img.moviepostershop.com/waiting-for-guffman-movie-poster-1996-1010258036.jpg",  # noqa
    "https://www.youtube.com/watch?v=fmkjNb3jiJc")

# a list of my favorite movies from the 90s - corresponds to the objects above
movie_list = [unforgiven, big_lebowski, pulp_fiction,
              true_romance, team_america, guffman]

# Generate and display the movies page
fresh_tomatoes.open_movies_page(movie_list)
