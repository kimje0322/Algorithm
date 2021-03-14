N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
ans = [0]*M
def backtracking(depth):
    if depth == M:
        print(' '.join(map(str, ans)))
        return
    overlap = 0
    for i in range(N):
        if overlap != num[i]:
            ans[depth] = num[i]
            overlap = num[i]
            backtracking(depth+1)
backtracking(0)