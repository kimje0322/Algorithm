def dp(n):
    for i in range(n):
        for j in range(0, i):
            if dy[j] < dy[i]:
                dy[i] += dy[j]



N = int(input())
data = list(map(int, input().split()))
maxV = 0
dy = [1]*N
dp(0)
print(dy)