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