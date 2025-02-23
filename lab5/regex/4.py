import re

def find_sequences(file):
    match = re.findall(r"\b[A-Z][a-z]+\b", file) #[a-z]+ — одна или более строчных букв (a–z)
    if match:
        return match
    else: return "No match"
    
with open("lab5/regex/row.txt", "r", encoding= "utf-8") as file:
    text = file.read()
    
print(find_sequences(text))