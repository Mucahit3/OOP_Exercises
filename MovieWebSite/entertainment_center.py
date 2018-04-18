import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.title)

avatar = media.Movie("Avatar",
               "A marine on an alien planet",
               "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.title)
#avatar.show_trailer()

never_back_down = media.Movie("Never Back Down",
               "A figthing and motivation movie",
               "https://upload.wikimedia.org/wikipedia/en/3/39/Never_back_down.jpg",
               "https://www.youtube.com/watch?v=2tc-RPjZRm8")

movies = [toy_story, avatar, never_back_down]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
