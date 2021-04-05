def dfs(n):
    if dy[n] > 0:
        return dy[n]
    if n < 3:
        return n
    else:
        dy[n] = dfs(n-1) + dfs(n-2)
    return dy[n]
n = int(input())
dy = [0]*(n+2)
print(dfs(n+1))