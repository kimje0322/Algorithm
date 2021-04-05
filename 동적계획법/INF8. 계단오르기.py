# 동적계획법 bottom-up : 작은 문제부터 큰 문제로 확장해나가는 것
# (재귀 top-down) - 넓은 의미에서 동적계획법
# rt => read text

# 재귀
# def dfs(n):
#     if dy[n] > 0:
#         return dy[n]
#     if n < 3:
#         return n
#     else:
#         dy[n] = dfs(n-1) + dfs(n-2)
#     return dy[n]


def dfs(num):
    for i in range(1,num+1):
        if i < 3:
            dy[i] = i
        else:
            dy[i] = dy[i-1]+dy[i-2]
    return dy[num]
n = int(input())
dy = [0]*(n+1)
print(dfs(n))
