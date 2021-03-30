import sys
import copy
input = sys.stdin.readline

def check(x,y,data,d):
    for i in d:
        nx, ny = x,y
        while True:
            # nx += dx[i]
            # ny += dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if data[nx][ny] == 6:
                    break
                elif data[nx][ny] == 0:
                    data[nx][ny] = '#'
                else:
                    break

def dfs(data, cnt):
    global result
    tmp = data[:]
    if cnt == cctvcnt:
        num = 0
        for i in range(N):
            num += tmp[i].count(0)
        result = min(result, num)
        return
    x,y,cctv = stack[cnt]
    for i in direction[cctv]:
        check(x,y,tmp,i)
        # tmp = data[:]

    stack.append((i,j))
    if data[i][j] == 1:
        pass
    elif data[i][j] == 2:
        pass
    return

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
stack = []
cctvcnt = 0
direction = []
ans = 9999999
for i in range(N):
    for j in range(M):
        if 0 < data[i][j] < 6:
            stack.append([i,j,data[i][j]])
            cctvcnt += 1
dfs(data, 0)