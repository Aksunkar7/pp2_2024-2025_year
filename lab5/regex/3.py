import re

def match_sequences(file):
    match = re.findall(r"\b[a-z]+_[a-z]+\b", file) # sdcn_asfsj типтегі стрингты қайтарады !кіші әріпте, [a-z]+ — одна или более строчных букв (a–z)
    if match:
        print(match)
        return "Match found"
    else: return "No match"
    
with open("lab5/regex/row.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(match_sequences(text))
