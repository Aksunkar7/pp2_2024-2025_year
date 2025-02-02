from dictionary import movies
def avg_imdb(movies):
    sum_of_imdb_rate = 0
    for movie in movies:
        sum_of_imdb_rate += movie["imdb"]
    return sum_of_imdb_rate/len(movies)

avg = avg_imdb(movies)
print(f"Average rate of movies: {avg:.2f}")  #   :.2f - 2ондық таңбамен шығарады