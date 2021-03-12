import sys
input = sys.stdin.readline

def f(idx):
    if idx == M:
        print(*ans)
        return

    for i in range(1, N+1):
        ans[idx] = i
        f(idx+1)


N, M = map(int, input().split())
ans = [0]*M
f(0)