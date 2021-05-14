def delivery(n):
    num = 0
    while n > 0:
        if n % 5 != 0:
            n -= 3
            if n < 0:
                return -1
            num += 1
        elif n % 5 == 0:
            n -= 5
            num += 1
        elif n % 5 != 0 and n % 3 != 0:
            return -1
    return num

# 재귀를 써야한다고 생각한 이유
# 5와 3을 계속해서 빼면서 0이 되는지 확인해야하기 때문에
#
# def dp(n):
#     if n <= 5:
#         return dp[n]
#

n = int(input())
# dp = [0]*(n+1)
# dp[3], dp[5] = 1, 1
# dp[4] = -1
print(delivery(n))