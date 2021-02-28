def bfs(s,e):
    queue = [s]
    visited[s] = 1

    while queue:
        cur = queue.pop(0)
        for i in range(V+1):
            if adj[cur][i] == 1 and visited[i] == 0:
                if i == e:
                    return visited[cur]
                else:
                    queue.append(i)
                    visited[i] = visited[cur] + 1
    return 0

for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    S, E = map(int, input().split())
    print('#%d %d' % (t, bfs(S,E)))

