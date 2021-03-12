import sys

def dfs(depth):
    if depth == M:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        # print(*ans)
        return
    for i in range(N):
        ans[depth] = num[i]
        dfs(depth+1)

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
ans = [0]*M
dfs(0)
