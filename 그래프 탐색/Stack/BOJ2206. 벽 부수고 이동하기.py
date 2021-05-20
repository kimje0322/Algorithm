from collections import deque
def bfs():
    queue = deque([])
    queue.append((0,0))
    crash = False
    while queue:
        y, x = queue.popleft()
        if y == N-1 and x == M-1:
            return visited[y][x]+1
        for dy, dx in direction:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if data[ny][nx] == '0':
                    queue.append((ny,nx))
                    visited[ny][nx] = visited[y][x] + 1
                elif crash == False:
                    queue.append((ny,nx))
                    visited[ny][nx] = visited[y][x] + 1
                    crash = True
    return -1

N, M = map(int, input().split())
data = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
print(bfs())
print(data)