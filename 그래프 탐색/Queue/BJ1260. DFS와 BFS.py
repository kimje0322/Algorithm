from collections import deque

# 두번째 코드
def dfs(v, adj, visited):
    visited[v] = True
    print(v, end=' ')

    for next in sorted(adj[v]):
        if not visited[next]:
            dfs(next, adj, visited)

def bfs(v, adj, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for i in sorted(adj[cur]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 첫번째 코드
# def dfs(s):
#     visited = [0]*(N+1)
#     stack = [s]
#     while stack:
#         cur = stack.pop()
#         if not visited[cur]:
#             print(cur, end=" ")
#         visited[cur] = 1
#         adj[cur].sort(reverse=True)
#         for next_node in adj[cur]:
#              if not visited[next_node]:
#                  stack.append(next_node)
#     print()
#
# def bfs(s):
#     visited = [0]*(N+1)
#     queue = [s]
#     while queue:
#         cur = queue.pop(0)
#         if not visited[cur]:
#             print(cur, end=" ")
#         visited[cur] = 1
#         adj[cur].sort()
#         for next_node in adj[cur]:
#              if not visited[next_node]:
#                  queue.append(next_node)

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
visited = [[0]*(N+1) for _ in range(2)]
dfs(V, adj, visited[0])
print()
bfs(V, adj, visited[1])
print()