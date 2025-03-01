import os

def checkPath(path):
    if os.path.exists(path):
        print(f"Readable: {'Yes' if os.access(path, os.R_OK) else 'No'}")  #Short condition "ternary operator"
        print(f"Writable: {'Yes' if os.access(path, os.W_OK) else 'No'}")  #'access'-path дің "os.W_OK" достубын тексереді
        print(f"Executable: {'Yes' if os.access(path, os.X_OK) else 'No'}")#Оқуға,жазуға,орындауға болады ма тексереміз
    else:
        print("Path does not exist")

path = input("Enter the path: ")
#папка берсек тек сол папканы қарайды ішіндегі файлдарга мән бермейді,файлдарды тексеру үшін жеке жеке алып шығу керек


checkPath(path)


