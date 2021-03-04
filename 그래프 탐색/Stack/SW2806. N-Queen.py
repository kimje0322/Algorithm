# 두번째 푼 코드
def possible(r,c):
    for x in range(r):
        if r-x == abs(queens[x]-c):
            return False
    return True

def nQueen(r):
    global cnt
    if N == r:
        cnt += 1
    for c in range(N):
        if visit[c]:
            continue
        if not possible(r,c):
            continue
        visit[c] = 1
        queens[r] = c
        nQueen(r+1)
        visit[c] = 0

for t in range(1, int(input())+1):
    N = int(input())
    queens = [0] * N
    visit = [0] * N
    cnt = 0
    nQueen(0)
    print('#%d %d' % (t, cnt))


# 첫번째 푼 코드
# 문제점
# cnt가 처음 1이 되고 나서 더이상 visit 초기화를 비롯한 queen 교체작업이 이뤄지지 않음
# 유망성 판단 부분은 다른 함수로 분리하는 것이 좋음

# def nQueen(k):
#     global queens, availablity, cnt
#     if k == N and len(queens) == N:
#         cnt += 1
#     else:
#         for i in range(N):
#             availablity = True
#             if visit[i] == 0:
#                 for formerQ in queens:
#                     if abs(k - formerQ[0]) == abs(i - formerQ[1]):
#                         availablity = False
#                         break
#             if visit[i] == 0 and availablity == True:
#                     # 여기서 continue하면 ? return 해야하나
#                     # return => k+1행에 대한 함수가 종료돼서 안 됨
#                     # continue => queens에 대한 for문만 종료
#                 visit[i] = 1
#                 queens.append((k,i))
#                 nQueen(k+1)
#             if i == N-1 and 0 < len(queens) < k+1:
#                 a, b = queens.pop()
#                 visit[b] = 0
# for t in range(1, int(input())+1):
#     N = int(input())
#     queens = []
#     cnt = 0
#     availablity = True
#     visit = [0] * N
#     nQueen(0)
#     print('#%d %d' % (t, cnt))