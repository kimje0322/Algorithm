# 처음 풀이에 대한 반례
# => 사이클이 생기는 경우

# def dfs(a):
#     global maxV
#     stack = [a]
#     visited[a] = 1
#     while stack:
#         cur = stack.pop()
#         for i in range(1, n+1):
#             if arr[cur][i] and visited[i] == 0:
#                 stack.append(i)
#                 visited[i] = visited[cur]+1
#     if visited[cur] > maxV:
#         maxV = visited[cur]
#     return

def dfs(cur_node, val):
    global maxV
    if maxV < val:
        maxV = val

    for next_node in range(1, n+1):
        if arr[cur_node][next_node] and not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node, val+1)
            visited[next_node] = 0


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    maxV = 0
    for i in range(m):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    for idx in range(1, n+1):
        # visited 초기화
        visited = [0] * (n + 1)
        visited[idx] = 1
        dfs(idx, 1)
    print('#%d %d' % (t, maxV))


# 첫 풀이에 대한 반례(사이클이 생기는 경우)
# visited 초기화를 함수호출 전뿐만 아니라 함수 안에서도 부분적으로 해줘야함
# 1
# 7 7
# 1 2
# 2 3
# 3 4
# 4 5
# 2 6
# 6 7
# 7 3


6 5
1 2
1 3
2 4
2 5
2 6