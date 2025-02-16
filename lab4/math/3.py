import math
n = float(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
area = (n*pow(l, 2))/4*math.tan(math.pi/n)
print(f"The area of the polygon is: {math.ceil(area)}")