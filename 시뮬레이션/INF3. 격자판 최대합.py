n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# 행, 열의 합
maxV = 0
for i in range(n):
    cnt1, cnt2 = 0, 0
    for j in range(n):
        cnt1 += board[i][j]
        cnt2 += board[j][i]
    tmp = max(cnt1, cnt2)
    if maxV < tmp:
        maxV = tmp

# 대각선1의 합
# cnt == n => break
cnt1, cnt2 = 0,0
for i in range(n):
    cnt1 += board[i][i]
    cnt2 += board[i][n-i-1]
# i = 0
# while i < n:
#     cnt1 += board[i][i]
#     i += 1
# 대각선2의 합
# i, j = 0, n-1
# while 0 <= i < n and 0 <= j < n:
#     cnt2 += board[i][j]
#     i += 1
#     j -= 1
print(max(maxV, cnt1, cnt2))