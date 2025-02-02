def toOunces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = int(input("gram: "))
print(toOunces(grams), "Ounces")