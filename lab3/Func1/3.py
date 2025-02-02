def solve(numheads, numlegs):
    # R*4 + Ch*2 = 94
    # Ch = 47 - 2R
    # Ch = 35 - R    
    # 47 - 2R = 35 - R
    # R = 47-35 = 12
    # Ch = 35-12 = 23
    # Formula: R = numlegs/2 - numheads
    R = numlegs//2 - numheads
    Ch = numheads - R
    print("Rabbits:", R, "Chickens:", Ch )

numheads, numlegs = int(input("NumHeads: ")), int(input("NumLegs: "))
solve(numheads,numlegs)