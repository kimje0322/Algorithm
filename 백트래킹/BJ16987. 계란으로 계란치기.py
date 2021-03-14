import sys
input = sys.stdin.readline
# from collections import deque

def backtracking(cur):
    global cnt
    if cur >= N:
        return
    # d 내구성 w 무게
    for next in range(cur,N):
        if data[next] != data[cur]:
            data[cur] = [data[next][1] - data[cur][0], data[cur][1]]
            data[next] = [data[cur][1] - data[next][0], data[next][1]]
            if data[cur][0] <= 0:
                data.pop(cur)
                cnt += 1
            if data[next][0] <= 0:
                data.pop(next)
                cnt += 1
        backtracking(cur+1)


N = int(input())
cnt = 0
data = [[] for _ in range(N)]
for i in range(N):
    data[i] = list(map(int, input().split()))
# data = deque(data)
print(data)
# visited = [1]+[0]*(N-1)
backtracking(0)
print(cnt)


# 현재 문제점: data를 변경시켜도 원래 data 리스트를 참조하고 있어서
# if len(data) > 1: 구문에서 빠져나오지 못하고 계속 걸린다.

# def backtracking(cur):
#     global cnt, data
#     if len(data) <= 1:
#         return
#     if cur >= N:
#         if maxCnt < cnt:
#             maxCnt = cnt
#         return
#     # d 내구성 w 무게
#     if len(data) > 1:
#         print(len(data))
#         for next in range(N):
#             if data[next] != data[cur]:
#                 data[cur] = [data[cur][0] - data[next][1], data[cur][1]]
#                 data[next] = [data[next][0] - data[cur][1], data[next][1]]
#                 if data[cur][0] <= 0:
#                     if next > cur:
#                         next = next -1
#                     data.pop(cur)
#                     cnt += 1
#                 if data[next][0] <= 0:
#                     data.pop(next)
#                     cnt += 1
#                 backtracking(cur+1)
#
#
# N =3
# cnt = 0
# maxCnt = 0
# data = [[8, 5], [1, 100], [3, 5]]
#
# # visited = [1]+[0]*(N-1)
# backtracking(0)
# print(cnt)