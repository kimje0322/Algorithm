import sys
input = sys.stdin.readline
# 문제 해결 키
# 0. 문제 이해 => 변하는 것과 변하지 않는 것 파악
# 1. 함수를 돌아가게 할 기준(인자) 설정
# 2. 종료 조건
# 3. 각종 경우의 수(예외) 처리

N = int(input())
egg_dur = []
egg_kg = []
for _ in range(N):
    dur, kg = map(int, input().split())
    egg_dur.append(dur)
    egg_kg.append(kg)
maxV = 0

def egg_break(idx, egg_dur, cnt):
    global maxV
    if idx == N:
        maxV = max(maxV, cnt)
        return
    if egg_dur[idx] <= 0:
        egg_break(idx+1, egg_dur, cnt)
        # 현재 idx 계란이 깨진 경우 다음 계란으로 넘기는 부분인데
        # 재귀함수 호출한 다음에 return 하는 이유가 뭐지?
        # return을 쓰지 않으면
        # 해당 idx는 이미 깨져서 for문 돌지 않아도 되는 상황임에도
        # for문을 포함한 (유망할 경우 돌아야하는)아래 코드를 쓸데 없이 돌게 됨
        return


    break_1more = False

    # idx=0 일 때 i = 1 ... 오른쪽으로 순차적으로만 이동가능한데
    # for문 쓰면 idx=0일때 i = 1,2,3... 전체 탐색하는거 아닌가?
    # 내구성 검사 if문에서 다 걸러짐
    for i in range(N):
        new_egg_dur = egg_dur[:]
        new_cnt = cnt
        if i != idx and egg_dur[idx] > 0 and egg_dur[i] > 0:
            break_1more = True
            new_egg_dur[idx] -= egg_kg[i]
            new_egg_dur[i] -= egg_kg[idx]
            if new_egg_dur[idx] <= 0:
                new_cnt += 1
            if new_egg_dur[i] <= 0:
                new_cnt += 1
            egg_break(idx+1, new_egg_dur, new_cnt)
    # 이 부분 어떤 경우인지 이해 잘 안감
    # 깨진 경우 다음 계란
    if not break_1more:
        egg_break(idx+1, egg_dur, cnt)

egg_break(0,egg_dur[:],0)
print(maxV)


# def backtracking(l,cur,data):
#     global cnt
#     if l >= N:
#         cnt = max(cnt, cur)
#         return
#     # d 내구성 w 무게
#     if data[l][0] > 0:
#         all_broken = True
#         for r in range(N):
#             if r == l or data[r][0] <= 0:
#                 continue
#             all_broken = False
#             data[l][0] -= data[r][1]
#             data[r][0] -= data[l][1]
#             n_cur = cur
#             n_cur += 1 if data[l][0] <= 0 else 0
#             n_cur += 1 if data[r][0] <= 0 else 0
#             backtracking(l+1, n_cur, data)
#             data[l][0] += data[r][1]
#             data[r][0] += data[l][1]
#         if all_broken:
#             backtracking(l+1, cur, data)
#     else:
#         backtracking(l+1, cur, data)
#
#
# N = int(input())
# cnt = 0
# data = [[] for _ in range(N)]
# for i in range(N):
#     data[i] = list(map(int, input().split()))
# backtracking(0,0,data)
# print(cnt)


# 현재 문제점: data를 변경시켜도 원래 data 리스트를 참조하고 있어서
# if len(data) > 1: 구문에서 빠져나오지 못하고 계속 걸린다.
# 슬라이싱으로 금방 해결
# 다음 문제점: 다음 함수 호출 조건, 함수 종료 조건 설정

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