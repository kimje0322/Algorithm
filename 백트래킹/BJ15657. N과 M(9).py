def dfs(depth):
    if depth == M:
        print(*ans)
        return
    for i in range(N):
        if selected[i]:
            continue
        selected[i] = 1
        ans[depth] = num[i]
        dfs(depth+1)

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
selected = [0]*N
ans = [0]*M
dfs(0)
