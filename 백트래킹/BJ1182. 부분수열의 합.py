N, S = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
selected = [0]*N

def backtraking(idx,sumV):
    global cnt
    if idx >= N:
        if sumV == S:
            cnt += 1
        return
    # selected[idx] = 1
    backtraking(idx+1, sumV+data[idx])
    # selected[idx] = 0
    backtraking(idx+1, sumV)

backtraking(0,0)
if S:
    print(cnt)
else:
    print(cnt-1)
