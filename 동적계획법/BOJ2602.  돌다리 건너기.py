# dp
def find():
    for j in range(n):
        dp[0][j][0] = 1
        dp[0][j][1] = 1
    for i in range(1, scroll_len):
        for j in range(1, n):
            if word[i-1] == angel[j-1]:
                dp[i][j][0] += dp[i-1][j-1][1]
            if word[i-1] == devil[j-1]:
                dp[i][j][1] += dp[i-1][j-1][0]
            dp[i][j][0] += dp[i][j-1][0]
            dp[i][j][1] += dp[i][j-1][1]
    return

# 완전탐색
# 돌다리 idx, 정답(word) idx, angle/devil
# def move(f,c,r):
#     global ans
#     if c == len(word):
#         return 1
#     if dp[f][c][r] > -1:
#         return dp[f][c][r]
#     total = 0
#     # devil
#     if r == 0:
#         for i in range(f, len(devil)):
#             if word[c] == devil[i]:
#                 total += move(i+1, c+1, 1)
#     # angel <= r:1
#     if r == 1 or c == 0:
#         for i in range(f, len(angel)):
#             if word[c] == angel[i]:
#                 total += move(i+1, c+1, 0)
#     dp[f][c][r] = total
#     return total

word = input()
devil = input()
angel = input()
n = len(angel)
scroll_len = len(word)
dp = [[[0 for _ in range(2)] for _ in range(101)] for _ in range(21)]
# print(find(0,0,0))