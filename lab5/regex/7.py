import re

def snake_to_camel(file):
    snake_to_camel = re.sub(r'_', '', file)   # Барлық "_" символдарын алып тастаймыз алмастырамыз
    return  snake_to_camel

with open("lab5/regex/row.txt", "r") as file:
    text = file.read()
print(snake_to_camel(text))  
