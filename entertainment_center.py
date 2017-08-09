
toy_story = media.Movie("Toy Story",
                        "A movie about a boy and his toys that come to life",
                        "G",
                        "http://www.rotoscopers.com/wp-content/uploads/2013/10/Toy-Story-Poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                        "A marine lands on an alien planet",
                        "PG-13",
                        "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8")

pulp_fiction = media.Movie("Pulp Fiction",
                            "Check out the big brain on Brad!",
                            "R",
                            "https://moviefiles.alphacoders.com/777/poster-thumb-77.jpg",
                            "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

true_romance = media.Movie("True Romance",
                            "Love conquers all",
                            "R",
                            "https://s-media-cache-ak0.pinimg.com/originals/20/96/52/2096528e05bee04ab065f27446b242cc.jpg",
                            "https://www.youtube.com/watch?v=0AIbZDBC8tk")

team_america = media.Movie("Team America World Police",
                            "Freedom isn't free.  It's gotta hefty fuckin fee",
                            "R",
                            "http://www.impawards.com/2004/posters/team_america_world_police_ver2.jpg",
                            "https://www.youtube.com/watch?v=RPBX47zSktc")

guffman = media.Movie("Waiting for Guffman",
                        "A community theatre waits for a New York Times reviewer",
                        "R",
                        "http://img.moviepostershop.com/waiting-for-guffman-movie-poster-1996-1010258036.jpg",
                        "https://www.youtube.com/watch?v=fmkjNb3jiJc")

movie_list = [toy_story, avatar, pulp_fiction, true_romance, team_america, guffman]

open_movies_page(movie_list)
