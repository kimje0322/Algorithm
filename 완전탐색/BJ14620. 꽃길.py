# sj 설정?

# 유효성 체크
def valid_check(i,j):
    # direction = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
    for y, x in direction:
        if i+y < 0 or i+y > N-1 or i+x < 0 or i+y > N-1 or visited[i+y][j+x]:
            return False
    return True

# 비용 더하기
def cal(i,j):
    result = 0
    for y, x in direction:
        result += cost[i+y][j+x]
    return result

# 시작할 행 위치, 꽃개수, 현재까지 더해진 가격
def dfs(si, cnt, tmp_cost):
    global minV
    if tmp_cost >= minV:
        return
    # 기저 영역
    if cnt == 3:
        minV = min(minV, tmp_cost)
        return
    for i in range(si, N-1):
        for j in range(1, N-1):
            if valid_check(i,j):
                for y, x in direction:
                    visited[i+y][j+x] = 1
                dfs(i, cnt+1, tmp_cost+cal(i,j))
                for y, x in direction:
                    visited[i+y][j+x] = 0

N = int(input())
minV = (N**2)*200
cost = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
direction = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
dfs(1,0,0)
print(minV)





# def check(y,x):
#     for d in range(5):
#         ny = y + dy[d]
#         nx = x + dx[d]
#         if ny < 0 or ny > N-1 or nx < 0 or nx > N-1 or visited[ny][nx]:
#             return False
#     return True
#
# def cal(y,x):
#     result = 0
#     for d in range(5):
#         ny = y + dy[d]
#         nx = x + dx[d]
#         result += coast[ny][nx]
#     return result
#
#
# def make_flower(cnt, tmp_coast):
#     global minV
#     if minV <= tmp_coast:
#         return
#     if cnt == 3:
#         minV = min(minV, tmp_coast)
#         return
#
#     for i in range(1,N-1):
#         for j in range(1,N-1):
#             if check(i,j):
#                 for d in range(5):
#                     visited[i+dy[d]][j+dx[d]] = 1
#                 make_flower(cnt+1,tmp_coast+cal(i,j))
# #                 for d in range(5):
# #                     visited[i+dy[d]][j+dx[d]] = 0
#     return
#
# N = int(input())
# coast = [list(map(int, input().split())) for _ in range(N)]
# minV =  200*(N**2)
# tmp_flower = 0
# visited = [[0]*N for _ in range(N)]
# dx, dy = [-1,1,0,0,0],[0,0,0,-1,1,0]
# make_flower(0,0)
# print(minV)
# -------------------

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