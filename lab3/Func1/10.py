def uniqueee(list):
    if not list:  # Егер тізім бос болса, бос тізімді қайтарамыз
        return []
    
    
    list.sort()               
    list2 = []
    for i in range(1,len(list)):
        if list[i] != list[i-1]:
            list2.append(list[i-1]) #алдыңғы элементке тең болмаса, алдыңғы элементті шығарамыз
    list2.append(list[-1])          #Соңғы элемент в любом случае қосылмағандықтан кез келген жағдайда оны қосамыз
    return list2

list = list(map(int, input().split()))
print(uniqueee(list))