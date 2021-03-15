import sys
input = sys.stdin.readline

def backtracking(l,cur,data):
    global cnt
    if l >= N:
        cnt = max(cnt, cur)
        return
    # d 내구성 w 무게
    if data[l][0] > 0:
        all_broken = True
        for r in range(N):
            if r == l or data[r][0] <= 0:
                continue
            all_broken = False
            data[l][0] -= data[r][1]
            data[r][0] -= data[l][1]
            n_cur = cur
            n_cur += 1 if data[l][0] <= 0 else 0
            n_cur += 1 if data[r][0] <= 0 else 0
            backtracking(l+1, n_cur, data)
            data[l][0] += data[r][1]
            data[r][0] += data[l][1]
        if all_broken:
            backtracking(l+1, cur, data)
    else:
        backtracking(l+1, cur, data)


N = int(input())
cnt = 0
data = [[] for _ in range(N)]
for i in range(N):
    data[i] = list(map(int, input().split()))
backtracking(0,0,data)
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