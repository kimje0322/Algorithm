def fibo(n):
    for i in range(n+1):
        if i <= 1:
            dp[i] = i
        else:
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input())
dp = [0]*(n+1)
print(fibo(n))