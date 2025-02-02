class string:
    def __init__(self, str):
        self.str = str
        
    def getString(self):
        print(self.str)
        
    def printString(self):
        print(self.str.upper())
        
str = string(input("Matindi engiz: "))
string.getString(str)
string.printString(str)
