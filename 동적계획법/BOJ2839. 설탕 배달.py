def delivery(n):
    for i in range(6, n+1):
        if dp[n] > dp[n-5] + 1:
            dp[n] = dp[n-5] + 1
        elif dp[n] > dp[n-3] + 1:
            dp[n] = dp[n-3] + 1
    return
# 재귀를 써야한다고 생각한 이유
# 
def dp(n):

    return

n = int(input())
dp = [0]*(n+1)
dp[3], dp[5] = 1, 1
dp[4] = -1
print(delivery(n))