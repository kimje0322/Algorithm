N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
ans = [0]*M
selected = [0]*N
def backtracking(depth,idx,N,M):
    if depth == M:
        print(' '.join(map(str, ans)))
        return
    overlap = 0
    for i in range(idx,N):
        if not selected[i] and overlap != num[i]:
            selected[i] = 1
            ans[depth] = num[i]
            overlap = num[i]
            backtracking(depth+1, i+1, N, M)
            selected[i] = 0

backtracking(0,0,N,M)