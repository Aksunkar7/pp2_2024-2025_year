is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, n))

numbers = list(map(int, input("Сандарды енгізіңіз:").split()))

# сортировка жасау filter - массивті толық is_prime қанағаттанатын мәндермен толтырады
prime_numbers = list(filter(is_prime, numbers)) #жаңа массивке салдық

print("Жай сандар:", prime_numbers)
