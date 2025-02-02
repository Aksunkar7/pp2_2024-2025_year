from dictionary import movies
def isAbove(movie):
    for x in movies:
        if x["name"] == movie:
            if x["imdb"] > 5.5:
                return True
    return False
    
movie = input("Name of movie: ")

print(isAbove(movie))