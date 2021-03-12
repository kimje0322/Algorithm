# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
def dfs(idx):
    if idx == M:
        print(*ans)
        return
    for i in range(1,N+1):
        if selected[i]:
            continue
        selected[i] = 1
        ans[idx] = i
        dfs(idx+1)
        for j in range(i+1, N+1):
            selected[j] = 0

N, M = map(int, input().split())
selected = [0]*(N+1)
ans = [0]*M
dfs(0)


# from itertools import combinations
# N, M = map(int, input().split())
# p = combinations(range(1, N+1), M)
# for i in p:
#     print(*i)