import sys
input = sys.stdin.readline
from collections import deque

# 코드 문제점
# visited 배열이 적절한 위치에서 초기화 되지 않음 << 이라고 생각했는데
# 이게 되네?
# 풀어놓고 이해가 안갔는데
# bfs는 목적지에 빨리 퍼져서 도달하는 순간 목적(최솟값)을 이룬 것이기 때문에
# 경로를 따라간다고 생각하면 안 되는 것 같음.

def bfs():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if maze[i][j] == '1' and not visited[i][j]:
                queue.append((i,j))
                while queue:
                    # 현재 위치 이동
                    y, x = queue.popleft()
                    if y == N-1 and x == M-1:
                        return visited[y][x] + 1
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        # 범위 내에 있고 방문안했으면
                        if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == '1':
                            if not visited[ny][nx]:
                                # queue에 추가
                                queue.append((ny,nx))
                                visited[ny][nx] = visited[y][x] + 1


N, M = map(int, input().split())
maze = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
print(bfs())