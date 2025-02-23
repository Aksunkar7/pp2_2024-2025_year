import re

def camel_to_snake(text):
    result = re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower() #\1_\2 → бірінші топ (кіші әріп) мен екінші топтың (үлкен әріп) арасына _ қояды.
    return result


with open("lab5/regex/row.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(camel_to_snake(text))
