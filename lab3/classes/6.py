class Prime:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def isPrime(self):
        is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, n)) 

        # сортировка жасау filter - массивті толық is_prime қанағаттанатын мәндермен толтырады
        prime_numbers = list(filter(is_prime, numbers)) #жаңа массивке салдық
        return prime_numbers
        
        
    
numbers = list(map(int, input("Сандарды енгізіңіз:").split()))

a = Prime(numbers)
print(a.isPrime())