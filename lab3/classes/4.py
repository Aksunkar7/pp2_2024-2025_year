import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print("X:", self.x, "Y:", self.y)
    
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
        
    def dist(self, other_point):
        print("Distance is:", math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2))
        
        
p1 = Point(int(input("X1:")), int(input("Y1:")))
p2 = Point(int(input("X2:")), int(input("Y2:")))

p1.show()
p2.show()

p1.move(int(input("New X1:")), int(input("New Y1:")))

p1.dist(p2)