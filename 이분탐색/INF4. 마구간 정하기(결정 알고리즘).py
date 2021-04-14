# 내 풀이
# 완전탐색으로 하려다가 걸림
def backtracking(idx):
    global maxV, data
    if idx == C:
        for i in range(C):
            if selected[i] == 1:
                data.append(horses[i])
        tmp = data[0]
        for j in range(1,C):
            maxV = max(maxV, data[j]-tmp)
        return
    for i in range(C):
        selected[i] = 1
        backtracking(idx+1)
        selected[i] = 0
        backtracking(idx+1)

N, C = map(int, input().split())
horses = []
data = []
# [False for _ in range(N)]
maxV = -1
for _ in range(N):
    horses.append(int(input()))
horses.sort()
selected = [0]*C
backtracking(0)
print(maxV)
