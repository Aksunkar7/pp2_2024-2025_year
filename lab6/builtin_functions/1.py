def multiply_list_elems(list):
    sum = 1
    for elem in list:
        sum *= elem
    return sum
    
a = list(map(int, input("Elems of list: ").split()))
print(multiply_list_elems(a))
