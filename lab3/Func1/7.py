def Three(numbers):
    for i in range(len(numbers)):
        if i!=len(numbers):  #соңғы элемент болып қалса i+1 қате береді
            if numbers[i] == 3 & numbers[i+1] == 3:
                return True
    return False
numbers = list(map(int, input("Тізімнің элементтерін енгіз:").split()))            
print(Three(numbers))