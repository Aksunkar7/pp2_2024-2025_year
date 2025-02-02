from dictionary import movies
def avg_of_category(category, movies):
    total_score_category = 0
    cnt = 0
    for movie in movies:
        if movie["category"].lower() == category.lower():  #Чтобы не обращать внимание на регистр
            total_score_category += movie["imdb"]
            cnt += 1
    return total_score_category / cnt if cnt!=0 else 0 # Егер категория табылмаса, 0 қайтарылады


category = input("Category engiz: ")
average_of_category = avg_of_category(category, movies)
print(f"avg_of_category = {average_of_category:.2f}")