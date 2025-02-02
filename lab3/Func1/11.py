def is_palind(soz):
    soz2 = soz[::-1]
    if soz == soz2:
        return True
    return False

soz = input("Sozdi engiz:")
if(is_palind(soz)):
    print("is Palindrome")
else: print("isn't Palindrome")    
