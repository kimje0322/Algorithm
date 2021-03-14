N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
selected = [0]*N
ans = [0]*M

def backtracking(depth, idx):
    if depth == M:
        print(' '.join(map(str, ans)))
        return
    overlap = 0
    for i in range(idx,N):
        if overlap != num[i]:
            ans[depth] = num[i]
            overlap = num[i]
            backtracking(depth+1, i)
            # selected[i] = 0
backtracking(0,0)