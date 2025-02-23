import re

def add_spaces(file):
    str = re.sub(r"\B(?=[A-Z])", " ", file) #\B(?=[A-Z]) бірінші сөздің алдына пробел қоймау үшін 
    return str.strip() 

    
with open("lab5/regex/row.txt", "r", encoding= "utf-8") as file:
    text = file.read()
    
print(add_spaces(text))