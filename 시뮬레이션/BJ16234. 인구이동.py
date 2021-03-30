import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    tmp = []
    tmp.append([i,j])
    while queue:
        x,y = queue.popleft()
        for r, c in direction:
            nx, ny = x + r, y + c
            # 다음 위치가 유효하고
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                # 인구 차이가 주어진 범위 내에 있으면
                if L <= abs(border[nx][ny] - border[x][y]) <= R:
                    # 방문 표시
                    visited[nx][ny] = 1
                    queue.append([nx,ny])
                    tmp.append([nx,ny])
    return tmp

N, L, R = map(int, input().split())
border = [list(map(int, input().split())) for _ in range(N)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
cnt = 0
while True:
    visited = [[0]*N for _ in range(N)]
    move = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                # 방문 국가 저장
                tmp = bfs(i,j)
                # 방문 국가가 2개 이상이면 인구 이동
                if len(tmp) >= 2:
                    move = True
                    # 인구 변경
                    num = sum(border[x][y] for x,y in tmp) // len(tmp)
                    for x,y in tmp:
                        border[x][y] = num
    if not move:
        break
    cnt += 1
print(cnt)