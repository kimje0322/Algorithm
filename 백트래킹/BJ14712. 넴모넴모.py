# 순서가 필요한 순열
# - for문안에서 v[i]=1 -> 재귀함수 -> v[i]=1
# - 외판원 2
# 순서가 필요없는 조합
# v[i]=1 -> 재귀함수 -> v[i]=1 -> 재귀함수
# - 부분수열의 합, 넴모넴모

N, M = map(int, input().split())
board = [[0]*M for _ in range(N)]
dx, dy = [1,1,0], [0,1,1]

def game(idx):
    global cnt, r, c
    nonCount = False
    # val = idx-1
    # r1 = val/M
    # c1 = val/M
    if 1 <= r < N and 1 <= c < M:
       if board[r-1][c-1] and board[r-1][c] and board[r][c-1]:
           return

    if idx == N*M:
        cnt += 1
        return

    for i in range(N):
        for j in range(M):
            board[i][j] = 1
            r, c = i, j
            game(idx+1)
            board[i][j] = 0
            r, c = i, j
            game(idx+1)

cnt = 0
r,c = 0,0
game(0)
print(cnt)

#     if idx == N*M:
#         for ele in stack:
#             if nonCount:
#                 return
#             cur_r, cur_c = ele
#             twotwo = 0
#             for d in range(3):
#                 if (cur_r+dx[d], cur_c+dy[d]) in stack:
#                     twotwo += 1
#                 if twotwo == 3:
#                     nonCount = True
#                     break
#         if nonCount:
#             cnt -= 1
#         return