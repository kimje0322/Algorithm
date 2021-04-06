n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
cnt = 0
for i in range(n):
    for j in range(n):
        flag = 1
        for y,x in direction:
            ny, nx = i+y, j+x
            if 0 <= ny < n and 0 <= nx < n and data[i][j] <= data[ny][nx]:
                flag = 0
                break
        if flag:
            cnt += 1
print(cnt)

