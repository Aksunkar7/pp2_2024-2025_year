def Even(n):
    num = 0
    for i in range(n):
        if i%2 == 0:
            yield i
  
a = int(input("Sandy engiz: "))      
evens = Even(a)

for ev in evens:
    print(ev)