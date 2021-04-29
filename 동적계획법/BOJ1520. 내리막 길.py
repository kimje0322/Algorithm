import sys
input = sys.stdin.readline

def dfs(y,x):
    if dp[y][x] > 0:
        return dp[y][x]
    else:
        for r, c in directions:
            ny, nx = y+r, x+c
            if 0 <= ny < N and 0 <= nx < M and road[y][x] > road[ny][nx]:
                dp[y][x] += dfs(ny,nx)
    return dp[y][x]

N, M = map(int, input().split())
directions = [(-1,0),(1,0),(-1,0),(1,0)]
road = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
print(dfs(0,0))