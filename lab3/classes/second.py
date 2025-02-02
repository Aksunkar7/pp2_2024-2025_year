class Shape:
    def __init__(self):
        pass
    
    def area(self):
        print("Area:", 0)
        
        
class Square(Shape):
    def __init__(self, length):
        super().__init__()        # Shape.__init__(self) dese de bolady, біз жазған вариант универсальный
        self.len = length
        
        
    def area(self):
        print("Area:", self.len * self.len)
    
a = Shape()
print(a.area())

# !!!!!!!!! Жалпы класс шақырған кезде инит ішіндегі аргументтерге қараймыз соған байланысты классқа береміз

square = Square(int(input("Length:"))) #Square классының ишиндеги инитке length аргументине мән береді,
                                        # ол " self.len = " барып сақталады

square.area() #square деген айнымалы объект болып есептеледі себебі ішінде классты сақтап отыр, area функциясы селфты  
              #қабылдайды яғни біздің енгізген length сосын area орындалады
