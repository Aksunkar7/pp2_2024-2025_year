def list_to_file(list):
    with open("aksungkar.txt", "w", encoding="utf-8") as file:
        for item in list:
            file.write(item + "\n")   # Әр элементті файлдың жаңа жолына жазамыз


list = list(input("Elements: ").split())
list_to_file(list)


