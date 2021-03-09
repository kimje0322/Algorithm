def dfs():
    


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
tmp = 0
ans = []
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adj[b].append(a)
for i in range(1, N+1):
    if not adj[i]: continue
    else:
        dfs(i)
