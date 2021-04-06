n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]
center = n//2
ans = 0
# i, j = 0, center
# while True:
#     ans += apple[i][j]
#     i += 1
#     j -= 1
i,s,e = 0, center, center
# 강의 코드는 while문 대신 i에 대한 for문, 나머지 동일
while i < n:
    for j in range(s, e + 1):
        ans += apple[i][j]
    if i < center:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
    i += 1
print(ans)