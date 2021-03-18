def check(y,x):
    for d in range(5):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or ny > N-1 or nx < 0 or nx > N-1 or visited[ny][nx]:
            return False
    return True

def cal(y,x):
    result = 0
    for d in range(5):
        ny = y + dy[d]
        nx = x + dx[d]
        result += coast[ny][nx]
    return result


def make_flower(cnt, tmp_coast):
    global minV
    if minV <= tmp_coast:
        return
    if cnt == 3:
        minV = min(minV, tmp_coast)
        return

    for i in range(1,N-1):
        for j in range(1,N-1):
            if check(i,j):
                visited[i][j] = 1
                for d in range(5):
                    visited[i+dy[d]][j+dx[d]] = 1
                make_flower(cnt+1,tmp_coast+cal(i,j))
                visited[i][j] = 0
                for d in range(5):
                    visited[i+dy[d]][j+dx[d]] = 0
    return

N = int(input())
coast = [list(map(int, input().split())) for _ in range(N)]
minV =  200*(N**2)
tmp_flower = 0
visited = [[0]*N for _ in range(N)]
dx, dy = [-1,1,0,0,0],[0,0,0,-1,1,0]
make_flower(0,0)
print(minV)


#     for i in range(1,N-1):
#         for j in range(1,N-1):
#             if not visited[i][j]:
#                 if not visited[i-1][j] and not visited[i+1][j] and not visited[i][j-1] and not visited[i][j+1]:
#                     visited[i][j] = 1
#                     visited[i-1][j], visited[i+1][j],visited[i][j-1], visited[i][j+1] = 1, 1, 1, 1
#                     tmp_flower += coast[i][j]+coast[i-1][j]+coast[i+1][j]+coast[i][j-1]+coast[i][j+1]
#                     make_flower(cnt+1, minV)
#                     visited[i][j] = 1
#                     visited[i - 1][j], visited[i + 1][j], visited[i][j - 1], visited[i][j+1] = 0,0,0,0
#                     tmp_flower += coast[i][j] + coast[i - 1][j] + coast[i + 1][j]+coast[i][j-1]+coast[i][j+1]