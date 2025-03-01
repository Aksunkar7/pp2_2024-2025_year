def copyFile(file, new_file):
    with open(file, "r", encoding="utf-8") as source:
        content = source.read()  #Барлық жолды оқып аламыз

    with open(new_file, "w", encoding="utf-8") as new:
        new.write(content)  # Сол жолдарды еңгіземіз

    print(f"Contents copied from {file} to {new_file}.")


file = f"{input('Бар файлдың path жаз: ')}" #Бұрыннан бар файл болу керек(мысалы- row.txt) әйтпесе 'r' файлды таба алмайды
newfile = f"{input('Көшіру керек файлды жаз: ')}.txt"
copyFile(file, newfile)