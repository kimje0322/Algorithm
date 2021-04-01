def dfs(n):
    # 가지치기
    if dy[n] > 0:
        return dy[n]
    # 기저 조건
    if n < 3:
        dy[n] = n
        return n
    else:
        dy[n] = dfs(n-1)+dfs(n-2)
        return dy[n]
n = 3
dy = [0]*(n+1)
print(dfs(n))