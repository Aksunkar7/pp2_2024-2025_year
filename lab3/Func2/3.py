from dictionary import movies
def Category(category,movies):
    movies_which_one_type_category = []
    for movie in movies:
        if movie["category"].lower() == category.lower():
            movies_which_one_type_category.append(movie)
    return movies_which_one_type_category

category = input("Category: ")
print(Category(category,movies))