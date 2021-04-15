def check(distance):
    cnt = 1
    ep = horses[0]
    for i in range(1, N):
        if horses[i] - ep >= distance:
            cnt += 1
            ep = horses[i]
    return cnt

N, C = map(int, input().split())
horses = []
for _ in range(N):
    horses.append(int(input()))
horses.sort()
lt, rt = horses[0], horses[N-1]
while lt <= rt:
    mid = (lt+rt)//2
    if check(mid) >= C:
        ans = mid
        lt = mid + 1
    else:
        rt = mid -1
print(ans)
# 완전탐색으로 하려다가 걸림

# def backtracking(idx):
#     global maxV, data
#     if idx == C:
#         for i in range(C):
#             if selected[i] == 1:
#                 data.append(horses[i])
#         tmp = data[0]
#         for j in range(1,C):
#             maxV = max(maxV, data[j]-tmp)
#         return
#     for i in range(C):
#         selected[i] = 1
#         backtracking(idx+1)
#         selected[i] = 0
#         backtracking(idx+1)