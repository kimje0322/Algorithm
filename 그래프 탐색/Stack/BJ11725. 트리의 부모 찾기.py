def dfs(s):
    stack = [s]
    while stack:
        cur = stack.pop()
        visited[cur] = 1
        for node in adj[cur]:
            if not visited[node]:
                parrent[node-2] = cur
                stack.append(node)

N = int(input())
adj = [[] for _ in range(N+1)]
visited = [0]*(N+1)
parrent = [0]*(N-1)
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
dfs(1)
for p in parrent:
    print(p)
