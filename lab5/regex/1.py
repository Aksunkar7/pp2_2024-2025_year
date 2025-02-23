import re

def match_string(file):
    match = re.findall(r"ab*", text)
    if match:  
        print(match)
        return "Match found"
    else:
        return "No match"
    
with open("lab5/regex/row.txt", "r", encoding="utf-8") as file:
    text = file.read()
   
print(match_string(text))


