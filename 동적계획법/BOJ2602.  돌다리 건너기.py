# dp

# 완전탐색
# 돌다리 idx, 정답(word) idx, angle/devil
def move(f,c,r):
    global ans
    if c == len(word):
        return 1
    if dp[f][c][r] > -1:
        return dp[f][c][r]
    total = 0
    # devil
    if r == 0:
        for i in range(f, len(devil)):
            if word[c] == devil[i]:
                total += move(i+1, c+1, 1)
    # angel <= r:1
    if r == 1 or c == 0:
        for i in range(f, len(angel)):
            if word[c] == angel[i]:
                total += move(i+1, c+1, 0)
    dp[f][c][r] = total
    return total

word = input()
devil = input()
angel = input()
n = len(angel)
dp = [[[-1 for _ in range(3)] for _ in range(n)] for _ in range(n)]
print(move(0,0,0))
