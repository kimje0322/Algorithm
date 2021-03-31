import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
# # stack 구현
# def dfs():
#     global cnt
#     for idx in range(1,len(data)):
#         if not visited[idx]:
#             if idx == data[idx]:
#                 cnt += 1
#             else:
#                 stack = []
#                 stack.append(data[idx])
#                 visited[idx] = 1
#                 while stack:
#                     cur = stack.pop()
#                     visited[cur] = 1
#                     if not visited[data[cur]]:
#                         stack.append(data[cur])
#                 cnt += 1
#     return cnt

# 재귀함수
def dfs(start):
    visited[start] = 1
    next_node = data[start]
    if not visited[next_node]:
        dfs(next_node)
    return

for _ in range(int(input())):
    N = int(input())
    data = [0]+list(map(int, input().split()))
    cnt = 0
    visited = [0]*(N+1)
    for idx in range(1, N+1):
        if not visited[idx]:
            dfs(idx)
            cnt += 1
    print(cnt)