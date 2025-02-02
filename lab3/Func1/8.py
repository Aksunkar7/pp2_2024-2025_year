def spy_game(nums):
    cnt = 0
    for i in nums:
        if i == 0:
            cnt+=1
        elif i == 7 and cnt > 1: # 0 саны 7ге дейін 2 рет немесе одан көп рет кездессе шарт орындалады
            print(True)
            break
        else: continue
    else:print(False)
nums = list(map(int, input().split()))
spy_game(nums)