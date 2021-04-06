n = int(input())
maxPrize = 0
for _ in range(n):
    prize = 0
    nums = list(input().split())
    nums.sort()
    a,b,c = map(int, nums)
    if a == b and b == c:
        prize = 10000 + (a * 1000)
    elif a == b or a == c:
    # elif (a == b and b!= c) or (a == c and a != b):
        prize = 1000 + (a * 100)
    # elif b == c and c != a:
    elif b == c:
        prize = 1000 + (b * 100)
    else:
        prize = c*100

    # cnt = [0]*7
    # for num in nums:
    #     cnt[num] += 1
    # prize = 0
    # for idx in range(1,7):
    #     if cnt[idx] == 3:
    #         prize = 10000 + (idx * 1000)
    #     elif cnt[idx] == 2:
    #         prize = 1000 + (idx * 100)
    #     elif cnt[idx] == 1:
    #         prize = idx*100
    if prize > maxPrize:
        maxPrize = prize
print(maxPrize)