from dictionary import movies
def all_above_movies(movies):
    above_movies = []
    for movie in movies:
        if movie["imdb"]>5.5:
            above_movies.append(movie)
    return above_movies
            
print("Sum of movies: ", len(all_above_movies(movies)))
print(all_above_movies(movies))