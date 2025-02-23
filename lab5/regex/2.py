import re

def match_str(file):
    match = re.findall(r"ab{2,3}", file) # b{2,3} минимум 2,3 рет кездесетін жағдайларды шығарады, a{1}автоматический тұр
    if match:
        print(match)
        return "Match found"
    else: 
        return "No match"
    
with open("lab5/regex/row.txt", "r", encoding="utf-8") as file:
    text = file.read()
   

print(match_str(text))  