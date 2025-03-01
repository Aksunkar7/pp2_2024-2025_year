def isPalindrome(string):
    x = slice(None, None, -1) #builtin funct, same as [::-1]
    return True if string == string[x] else False 

str = input("String: ") #also 
print(isPalindrome(str))