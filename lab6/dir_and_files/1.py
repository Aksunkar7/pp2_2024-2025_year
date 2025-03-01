import os

def list_only_directories(path):
    print("\nOnly Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)): #path бен item ды біріктіреді "isdir"-папка ма тексереді
            print(item)

def list_only_files(path):
    print("\nOnly Files:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):#path бен item ды біріктіреді "isfile"- file ма тексереді
            print(item)

def list_all_items(path):
    print("\nAll Directories and Files:")
    for item in os.listdir(path): # Барлық элементтерді шығарады
        print(item)


path = input("Directory path: ")


if os.path.exists(path) and os.path.isdir(path): # Путьтің және папканың бар-жоғын тексеру
#Функцияларды шақыру
    list_only_directories(path) 
    list_only_files(path)                 
    list_all_items(path)
else:
    print("Invalid path or the path is not a directory.")
