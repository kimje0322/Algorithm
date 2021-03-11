import sys
input = sys.stdin.readline

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
def check(idx, n, m):
    if idx == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return
    for i in range(1, n+1):
        if selected[i]:
            continue
        selected[i] = 1
        ans[idx] = i
        check(idx+1, n, m)
        selected[i] = 0

N, M = map(int, input().split())
selected = [0]*(N+1)
ans = [0]*M
check(0,N,M)

# 1 2는 되지만 2 1 바뀐 순서 수열은 안됨
# def permutation(n):
#     if n == N+1:
#         if sum(selected) == M:
#             for idx in range(1, N+1):
#                 if selected[idx]:
#                     print(idx, end=" ")
#             print()
#         return
#     selected[n] = 1
#     permutation(n+1)
#     selected[n] = 0
#     permutation(n+1)