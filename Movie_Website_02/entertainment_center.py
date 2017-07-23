import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

oceans_11 = media.Movie("Oceans 11",
                        "A group of friends pull off a casino heist",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/6/68/Ocean%27s_Eleven_2001_Poster.jpg/220px-Ocean%27s_Eleven_2001_Poster.jpg",
                        "https://www.youtube.com/watch?v=imm6OR605UI")

helvetica = media.Movie("Helvetica",
                        "The background on one of the world's most iconic typefaces",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Helvetica-film.JPG/220px-Helvetica-film.JPG",
                        "https://www.youtube.com/watch?v=wkoX0pEwSCw")

hot_fuzz = media.Movie("Hot Fuzz",
                        "An elite cop gets relocated to the country",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c9/HotFuzzUKposter.jpg/220px-HotFuzzUKposter.jpg",
                        "https://www.youtube.com/watch?v=ayTnvVpj9t4")

dark_knight = media.Movie("The Dark Knight",
                            "Batman is back and awesome and shit",
                            "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                            "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [toy_story, avatar, oceans_11, helvetica, hot_fuzz, dark_knight]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
