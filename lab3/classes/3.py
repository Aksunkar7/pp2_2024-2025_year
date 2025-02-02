# from second import Shape # 2ші файлдағы кодтар запускаться етип кетеди
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        print("Area:", 0)
        
        
class Rectangle(Shape):
    def __init__(self, length, width):
        self.len = length
        self.wid = width
    
    def area(self):
        print("Area of rectangle:", self.len*self.wid)
        
Rect = Rectangle(int(input("Length:")), int(input("Width:")))
Rect.area()