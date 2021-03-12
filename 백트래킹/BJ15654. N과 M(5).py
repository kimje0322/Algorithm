import sys
input = sys.stdin.readline

def f(depth):
    if depth == M:
        print(*ans)
        return

    for i in range(N):
        if selected[i]:
            continue
        selected[i] = 1
        ans[depth] = num[i]
        f(depth+1)
        selected[i] = 0

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
selected = [0]*N
ans = [0]*M
f(0)