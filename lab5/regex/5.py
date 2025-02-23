import re

#a дан басталып b дан аяқталатын жолды табу программасы
def find_sequences(file):
    match = re.findall(r"\b[a].*[b]\b", file) #[a-z]+ — одна или более строчных букв (a–z), " .* "кез келген символдар санына шектеу жоқ
    if match:
        return match
    else: return "No match"
    
with open("lab5/regex/row.txt", "r", encoding= "utf-8") as file:
    text = file.read()
    
print(find_sequences(text))