import re

def replace_spaces(file):
    match = re.sub(r"[ ,.]", ":", file)
    if match:
        return match
    
with open("lab5/regex/row.txt", "r", encoding= "utf-8") as file:
    text = file.read()

print(replace_spaces(text))