def NfromDown(n):
    for num in range(n, -1, -1):
        yield num
        
a = int(input("Sandy engiz: "))

for nums in NfromDown(a):
    print(nums, end=" ")