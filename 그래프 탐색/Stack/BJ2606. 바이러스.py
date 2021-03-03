def dfs(n):
    while stack:
        cur = stack.pop()
        visited[cur] = 1
        for next_node in adj[cur]:
            if not visited[next_node]:
                stack.append(next_node)
    return sum(visited)-1

computer = int(input())
edge = int(input())
adj = [[] for _ in range(computer+1)]
for _ in range(edge):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
stack = [1]
visited = [0]*(computer+1)
print(dfs(1))
