def filter_prime(numbers):
    for x in numbers:
        if x < 2:
            continue 
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                break 
        else:
            print(x, end=" ")  # Егер цикл break-ке түспесе, жай сан

numbers = list(map(int, input("Сандарды енгізіңіз: ").split()))
filter_prime(numbers)
