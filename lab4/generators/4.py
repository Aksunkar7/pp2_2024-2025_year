def squares(a, b):
    for num in range(a, b+1):
        yield num**2
      
      
a = int(input("Bastapky sandy engiz: "))
b = int(input("Songy sandy engiz: "))    
Sq = squares(a, b)
for s in Sq:
    print(s, end=" ")