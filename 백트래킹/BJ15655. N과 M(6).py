# 방법1. 함수 인자로 다음 반복문 시작 범위 지정 (속도: 64ms)
def dfs(depth, idx):
    if depth == M:
        print(*ans)
        return
    for i in range(idx, N):
        if selected[i]:
            continue
        selected[i] = 1
        ans[depth] = num[i]
        dfs(depth+1, i+1)
        selected[i] = 0
# 방법2. selected 함수 0 표시할때 새로운 for문 범위 지정 (속도: 68ms)
# def dfs(depth):
#     if depth == M:
#         print(*ans)
#         return
#     for i in range(N):
#         if selected[i]:
#             continue
#         selected[i] = 1
#         ans[depth] = num[i]
#         dfs(depth+1)
#         for j in range(i+1, N):
#             selected[j] = 0

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
ans = [0]*M
selected = [0]*N
dfs(0,0)
