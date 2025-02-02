import math
#4/3*Pi*R**3
def volume_of_sphere(R):
    return 4/3*math.pi*R**3

R = int(input())
print(volume_of_sphere(R))