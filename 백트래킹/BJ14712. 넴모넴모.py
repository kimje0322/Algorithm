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
    global cnt, stack
    nonCount = False
    if idx == N*M:
        for ele in stack:
            if nonCount:
                return
            cur_r, cur_c = ele
            twotwo = 0
            for d in range(3):
                if (cur_r+dx[d], cur_c+dy[d]) in stack:
                    twotwo += 1
                if twotwo == 3:
                    nonCount = True
                    break
        if nonCount:
            cnt -= 1
        return

    for i in range(N):
        for j in range(M):
            if not board[i][j]:
                board[i][j] = 1
                stack.append((i,j))
                game(idx+1)
                board[i][j] = 0
                stack.pop()
stack = []
cnt = 2**(N*M)
# board [0,0] = 1
game(0)
print(cnt)

