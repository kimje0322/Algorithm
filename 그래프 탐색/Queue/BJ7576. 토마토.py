# a.count(x) 시간복잡도: O(n)
# len(a) 시간복잡도: O(1)

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    # unriped = sum([row.count(0) for row in tomato])
    # if unriped == 0:
    #     return 0

    if len(queue) == M * N:
        return 0
    while queue:
        cur_r, cur_c = queue.popleft()
        for d in range(4):
            nr, nc = cur_r + dx[d], cur_c + dy[d]
            if 0 <= nr < N and 0 <= nc < M:
                if not tomato[nr][nc]:
                    tomato[nr][nc] = 1
                    queue.append((nr,nc))
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
    maxV = 0
    for i in range(N):
        for j in range(M):
            if not tomato[i][j]:
                return -1
            if visited[i][j] >= maxV:
                maxV = visited[i][j]
    return maxV

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1,-1,0,0], [0,0,1,-1]
visited = [[0]*M for _ in range(N)]
queue = deque()
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 1:
            queue.append((r, c))
print(bfs())
