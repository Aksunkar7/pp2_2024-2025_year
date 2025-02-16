def Square(N):
    num = 1
    while 1:
        if num > N:
            return
        else:
            yield num**2 #осы санды шығарады да тоқтап қалады
            num+=1       #тағы да некст болганда жалгасады +1 болып
            
a = int(input("Sandy engiz: "))
square = Square(a)
print(next(square))
for sq in square:  
    print(sq, end=" ")

        
