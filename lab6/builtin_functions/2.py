def number_of_upper_lowers(str):
    numUpper = 0
    numLower = 0
    for letter in str:
        if letter.islower():
            numLower += 1
        if letter.isupper():
            numUpper += 1
    print(f"Upper letters: {numUpper}")
    print(f"Lower letters: {numLower}")
    
str = input("String: ")
number_of_upper_lowers(str)