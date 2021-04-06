def reverse(x):
    res = 0
    while x > 0:
        tmp = x % 10
        x //= 10
        res = res*10+tmp
    return res

ch = [0]*(100001)
ch[1] = 1
for i in range(2, 100001):
    if not ch[i]:
        for j in range(i+i, 100001, i):
            ch[j] = 1

def isPrime(x):
    if not ch[x]:
        return True
    return False

n = int(input())
nums = list(map(int, input().split()))
for num in nums:
    tmp = reverse(num)
    # print(isPrime(tmp))
    if isPrime(tmp):
        print(tmp, end=" ")