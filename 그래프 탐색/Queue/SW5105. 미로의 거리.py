def check(x,y):
    queue = list()
    queue.append((x,y))
    while queue:
        cr, cc = queue.pop(0)
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if maze[nr][nc] == 3:
                    return visited[cr][cc]
                elif maze[nr][nc] == 0 and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[cr][cc] + 1
    return 0

for t in range(1, int(input())+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                x, y = i, j
                break
    print('#%d %d' % (t,check(x,y)))