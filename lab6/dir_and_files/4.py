def cntLines(file):
    try: #Осы жерде қате шықса тоқтамайды, ексепт блогына өтеді
        with open(filename, 'r', encoding='utf-8') as file: # Файлды ашу
            lines = file.readlines() # Барлық жолдарды оқу
            
            print(f"Number of lines: {len(lines)}") # Жол санын есептеу
    except FileNotFoundError:
        print("File not found.")
        
        
filename = input("Enter the filename: ")
cntLines(filename)

