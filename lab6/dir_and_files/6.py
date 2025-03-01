import string

def creating_files():
    
    # Барлық бас әріптерді аламыз 
    letters = string.ascii_uppercase   # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for letter in letters:
        filename = f"{letter}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"This is file {filename}\n")  # Бос болмас үшін жай файлдың атын жазамыз

    print("26 files created successfully")
    
creating_files()
