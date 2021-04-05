n, m = map(int, input().split())
cnt = [0]*(n+m+1)
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j] += 1
maxV = max(cnt)
ans = []
for idx in range(len(cnt)):
    if cnt[idx] == maxV:
        ans.append(idx)
print(*ans)