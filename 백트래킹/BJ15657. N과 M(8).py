import sys
def dfs(depth):
    if depth == M:
        sys.stdout.write(' '.join(map(str, ans))+'\n')
        return
    for i in range(N):
        if selected[i]:
            continue
        ans[depth] = num[i]
        dfs(depth+1)
        selected[i] = 1
        for j in range(i+1, N):
            selected[j] = 0

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
selected = [0]*N
ans = [0]*M
dfs(0)
