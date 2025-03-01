import os

def check_path(path):
    if os.path.exists(path):  # Путь бар-жоғын тексеру
        print("Path exists!")

        filename = os.path.basename(path) # Файл атын шығару, ең соңғы бөлігін шығарады сол файл немесе папка аты
        print(f"Filename: {filename}")

        directory = os.path.dirname(path) # Директория атын шығару, соңғы бөлікке дейінгі жол
        print(f"Directory: {directory}")

    else:
        print("Path does not exist.")



path = input("Enter the path: ")
check_path(path)
