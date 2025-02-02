from itertools import permutations #  берілген элементтердің барлық мүмкін ретін көреді.

def print_permutations(string):
    list = permutations(string)    # Барлық мүмкін жағдайларды қабылдап алады
    for x in list:                 # Әр элементті шығарады
        for i in x:                 
            print(i, end="")       # Әр элементті бір біріне қосады 
        print(end="\n")            # Әр сөзден кейін жол ауыстырады

str = input("Enter a string: ")  # Сөзді енгіз
print_permutations(str)
