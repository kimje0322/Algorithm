# 목표 8:30
def dfs(x,y):
    stack.append((x,y))
    while stack:
        rc, cc = stack.pop()
        visited[rc][cc] = 1
        for d in range(4):
            nr, nc = rc+dx[d], cc+dy[d]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == '3':
                    return 1
                elif maze[nr][nc] == '0' and visited[nr][nc] == 0:
                    stack.append((nr, nc))
    return 0

for t in range(1, int(input())+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    # maze = [input() for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    stack = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                print('#%d %d' % (t, dfs(i,j)))
                break