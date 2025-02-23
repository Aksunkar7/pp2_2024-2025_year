import re

def split_before_uppers(file):
    split = re.split(r'(?=[A-Z])', text)
    return  split

    
with open("lab5/regex/row.txt", "r", encoding= "utf-8") as file:
    text = file.read()
    
print(split_before_uppers(text))