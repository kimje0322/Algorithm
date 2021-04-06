from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    # 0왼쪽, 1오른쪽
    row, direction, c = map(int, input().split())
    row = row - 1
    if direction == 0:
        for i in range(c):
            tmp = board[row].pop(0)
            board[row].append(tmp)
    # 아래와 같이 슬라이싱해서 붙이면 이동이 n 보다 커질때 조건을 만족시키지 모샇ㅁ
        # board[row] = board[row][c:]+board[row][:c]
    elif direction == 1:
        for i in range(c):
            tmp = board[row].pop()
            board[row].insert(0,tmp)
        # board[row] = board[row][-c:]+board[row][:-c]
s,e = 0,n-1
ans = 0
for i in range(n):
    for j in range(s,e+1):
        ans += board[i][j]
    if i < n//2:
        s += 1
        e -= 1
    elif i >= n//2:
        s -= 1
        e += 1
print(ans)
