# 미세먼지 확산
def diffusion(r,c):
    if data[r][c] // 5 >= 1:
        val = data[r][c] // 5
        for dir in direction:
            i, j = dir
            if 0 <= r+i < R and 0 <= c+j < C and data[r+i][c+j] >= 0:
                tmp[r+i][c+j] += val
                data[r][c] -= val
    return

# 공기청정기 작동
# 다시 풀기
def cleaning():
    cnt = 0
    while cnt != T:
        # up 아랫줄
        c = C-1
        # 위칸-하단우측
        temp = data[cleaner-1][c]
        while c > 0 :
            if data[cleaner-1][c-1] == -1:
                data[cleaner-1][c] = 0
            else:
                data[cleaner-1][c] = data[cleaner-1][c-1]
            c -= 1
        # up 오른쪽줄
        r = 0
        # 위칸-상단우측 // c =
        temp1 = data[0][C-1]
        while r < cleaner - 1:
            if r == cleaner-2:
                data[r][C-1] = temp
            else:
                data[r][C-1] = data[r+1][C-1]
            r += 1
        # up 윗줄
        # 위칸-상단좌측
        temp2 = data[0][0]
        c = 0
        while c < C-1:
            if c == C-2:
                data[0][c] = temp1
            else:
                data[0][c] = data[0][c+1]
            c += 1
        # up 왼쪽줄
        r = cleaner - 2
        while r >= 1:
            if r == 1:
                data[r][0] = temp2
            else:
                data[r][0] = data[r-1][0]
            r -= 1
        # down 윗줄
        c = C - 1
        # 아래칸-상단우측
        temp = data[cleaner][c]
        while c > 0:
            if data[cleaner][c - 1] == -1:
                data[cleaner][c] = 0
            else:
                data[cleaner][c] = data[cleaner][c - 1]
            c -= 1
        # down 오른쪽줄
        r = R-1
        # 아래칸-하단우측
        temp1 = data[R-1][C-1]
        while r >= cleaner + 1:
            if r == cleaner + 1:
                data[r][C - 1] = temp
            else:
                data[r][C - 1] = data[r - 1][C - 1]
            r -= 1
        # down 아랫줄
        # 아래칸-하단좌측
        temp2 = data[R-1][0]
        c = 0
        while c < C - 1:
            if c == C - 2:
                data[R-1][c] = temp1
            else:
                data[R-1][c] = data[R-1][c + 1]
            c += 1
        # down 왼쪽줄
        r = cleaner + 1
        while r > R:
            if r - 1 == cleaner:
                data[r][0] = 0
            else:
                data[r][0] = data[r + 1][0]
            r += 1
        cnt += 1
    return

R, C, T = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(R)]
tmp = [[0]*C for _ in range(R)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
# 공기청정기 행(r) 아랫부분
cleaner = 0
# 미세먼지 존재 구간
dust = []

for y in range(R):
    for x in range(C):
        if data[y][x] > 0:
            dust.append((y,x))
        elif data[y][x] == -1:
            cleaner = y
while dust:
    y,x = dust.pop()
    diffusion(y,x)
for i in range(R):
    for j in range(C):
        data[i][j] += tmp[i][j]
cleaning()
ans = 0
for r in range(R):
    ans += sum(data[r])
print(ans+2)