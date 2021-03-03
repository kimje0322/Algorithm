def dfs(cur_node,val):
    global maxV
    if maxV < val:
        maxV = val

    for next_node in range(1, n+1):
        if nodes[cur_node][next_node] and not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node, val+1)
            visited[next_node] = 0

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    nodes = [[0]*(n+1) for _ in range(n+1)]
    maxV = 0
    for i in range(m):
        a, b = map(int, input().split())
        nodes[a][b] = 1
        nodes[b][a] = 1
    for idx in range(n+1):
        visited = [0]*(n+1)
        visited[idx] = 1
        dfs(idx,1)
    print('#%d %d' % (t, maxV))

# def dfs(cur_node, val):
#     global maxV
#     if maxV < val:
#         maxV = val
#     for next_node in range(1, n+1):
#         if nodes[cur_node][next_node] and not visited[next_node]:
#             visited[next_node] = 1
#             dfs(next_node, val+1)
#             visited[next_node] = 0
#
# for t in range(1, int(input())+1):
#     n, m = map(int, input().split())
#     nodes = [[0]*(n+1) for _ in range(n+1)]
#     maxV = 0
#     for i in range(m):
#         a, b = map(int, input().split())
#         nodes[a][b] = 1
#         nodes[b][a] = 1
#     for idx in range(1, n+1):
#         visited = [0]*(n+1)
#         visited[idx] = 1
#         dfs(idx, 1)
#     print('#%d %d' % (t, maxV))