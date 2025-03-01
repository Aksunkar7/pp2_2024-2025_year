import time

def find_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)#Миллисекундты секундқа ауыстырып,
                                   #сонша уақыт бағдарламаны тоқтатып тұрады
    return number ** 0.5

number = float(input("Number: ")) #25.5 Дегендей ондық сандарды қабылдауға мүмкіндік береміз
milliseconds = int(input("Millisecond: ")) #көбіне нақты уақыт аралығы бүтін санмен беріледі.

result = find_sqrt(number, milliseconds)
print(f"Square root of {number} after {milliseconds} miliseconds is {result}")
