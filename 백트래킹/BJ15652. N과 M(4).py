# def f(idx):
#     if idx == M:
#         print(*ans)
#         return
#
#     for i in range(1, N+1):
#         if selected[i]:
#             continue
#         ans[idx] = i
#         f(idx+1)
#         selected[i] = 1
#         for j in range(i+1,N+1):
#             selected[j] = 0

# 다른 사람 풀이
def f(depth, idx):
    if depth == M:
        print(*ans)
        return
    for i in range(idx, N):
        ans.append(i+1)
        f(depth+1, i)
        ans.pop()
N, M = map(int, input().split())
ans = []
selected = [0]*(N+1)
f(0,0)