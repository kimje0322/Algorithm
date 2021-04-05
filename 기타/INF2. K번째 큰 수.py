n, k = map(int, input().split())
num = list(map(int, input().split()))
res = set()
for i in range(n-2):
    for j in range(i+1, n-1):
        for l in range(j+1, n):
            res.add(num[i]+num[j]+num[l])
# [11, 13, 15, 23, 26, 33, 34, 42, 45, 65]
res = list(res)
res.sort(reverse=True)
print(res[k-1])