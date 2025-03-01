import os

def delete_file(file):

    if os.path.exists(path) and os.path.isfile(path): # аталған директория бар ма және ол файл ма тексеру
        
        if os.access(path, os.R_OK) and os.access(path, os.W_OK): #Рұқсат болмаса өшіре алмаймыз, өзгертуге болмайды
            os.remove(path) # Файлды өшіру
            print(f"File '{path}' has been deleted.")           
        else:
            print(f"No permission to delete the file: '{path}'") #Өшіруге рұқсат болмаса
    else:
        print(f"File does not exist: '{path}'") #Аталған файлдың болмауы

path = input("Enter the file path to delete: ")
delete_file(path)

