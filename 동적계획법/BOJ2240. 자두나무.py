# t초 동안 떨어지는 자두, 최대 w번 움직임
T, W = map(int, input().split())
tree = [int(input()) for _ in range(T)]
dp = [[0]*W for _ in range(T)]
current = 1
for w in range(W):
    cnt = 0
    idx = 0
    while idx < T:
        move = False
        while True:
            if current == tree[idx]:
                cnt += 1
            elif current != tree[idx]:
                if not move:
                    current = 2 if current == 1 else 2
                    move = True
                    cnt += 1
                elif move:
                    dp[idx][w] = cnt
                    break
            idx += 1


# 답
# T, W = map(int, input().split())
#     plums = [0]
#     for i in range(T):
#         plums.append(int(sys.stdin.readline()))
#
#     dp = [[0]*(W+1) for _ in range(T+1)]
#
#     for i in range(1, T+1):
#         # 한번도 움직이지 않았을 때(dp[i][0]을 채우는 과정)
#         if plums[i] == 1:  # 자두가 1번에서 떨어질 때만 받아 먹을 수 있다.
#             dp[i][0] = dp[i-1][0] + 1
#         else:
#             dp[i][0] = dp[i-1][0]
#
#         # 이동 횟수를 1번부터 W 번까지 움직이면서 체크
#         for j in range(1, W+1):
#             if j > i:
#                 break
#
#             # 자두가 1번에서 떨어지고, 그것을 받아 먹기
#             if plums[i] == 1 and j % 2 == 0:
#                 # 움직여서 받아먹을 것인가, 현재위치에서 받아먹을 것인가
#                 # 어짜피 이동한 횟수는 같다(지금 이동하거나 이전에 이동했거나)
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
#
#             # 자두가 2번에서 떨어지고, 그것을 받아 먹기
#             elif plums[i] == 2 and j % 2 == 1:
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
#
#             # 그 외 - 안먹는다 - 그대로 있거나 움직여서 안먹음
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
#
#     print(max(dp[-1]))