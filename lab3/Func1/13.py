import random
print("Hello! What's your name?")
name = input("Name: ")
num = random.randint(1,20)
print(name)
print("Well, " + name + " I am thinking of a number between 1 and 20.\n" + "Take a guess.")
cnt = 0
while(1):
    cnt+=1
    number = int(input())
    if number > num:
        print("The number is too high\n" + "Take a guess.")
        
    elif number < num:
        print("The number is too low\n" + "Take a guess.")
    else:
        print("Good job, " + name + "! You guessed my number in", cnt, "guesses!")
        break
        
