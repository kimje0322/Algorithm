import sys
input = sys.stdin.readline
def dfs(s,idx):
    global minV, sumV
    if idx >= N-1 and sum(visited) == N:
        # sumV += arr[s][start]
        if arr[s][start] and minV > sumV + arr[s][start]:
            minV = sumV + arr[s][start]
        # sumV -= arr[s][start]
        return

    for next in range(N):
        if arr[s][next] and not visited[next]:
            visited[next] = 1
            sumV += arr[s][next]
            dfs(next, idx+1)
            visited[next] = 0
            sumV -= arr[s][next]

N = int(input())
visited = [0]*N
sumV = 0
minV = 99999999
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    start = i
    visited[i] = 1
    dfs(i,0)
# print(arr)
print(minV)

# arr = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
# 아래 1, 2의 차이가 궁금함.
# 1은 for문 안에 있을 때 i가 바뀌니까 함수 호출해줄 필요없는 것 같고
# 2는 for문 돌아가지 않을 때인듯

# 1은 순서 상관있는 순열, 2는 순서 상관 없는 조합일까하는 추측도 해봤지만 아닌듯

# 1.
# visited[i] = 1
# f(idx+1, sumV+num[i])
# visited[i] = 0

# 2.
# visited[i] = 0
# f(idx+1, sumV+num[i])
# visited[i] = 1
# f(idx+1, sumV)

# 실패 코드
# global minV
# if idx >= N and sum(visited) ==N:
#     if minV > sumV:
#         minV = sumV
#         return

# for next in range(N):
#     if arr[next] and not visited[next]:
#         visited[next] = 1
#         dfs(next, idx+1, sumV+arr[next])
#         visited[next] = 0
#         dfs(next, idx+1, sumV)
