def divis(n):
    for i in range(n+1):
        if i%3 == 0 and i%4 == 0:
            yield i
        i += 1
        
a = int(input("Sandy engiz: "))        
nums = divis(a)

for num in nums:
    print(num)