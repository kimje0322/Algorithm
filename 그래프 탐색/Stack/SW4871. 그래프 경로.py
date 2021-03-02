def dfs(s,g):
    stack = [s]
    while stack:
        cur = stack.pop()
        visited[cur] = 1
        for i in adj[cur]:
            if i == g:
                return 1
            if visited[i] == 0:
                stack.append(i)
    return 0


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for i in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
    S, G = map(int, input().split())
    print('#%d %d' % (t, dfs(S,G)))