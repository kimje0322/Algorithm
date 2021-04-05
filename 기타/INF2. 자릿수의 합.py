n = int(input())
nums = list(map(int, input().split()))
def digit_sum(x):
    sumV = 0
    while x > 0:
        sumV += x % 10
        x //= 10
    return sumV
ans = 0
maxV = 0
for num in nums:
    tmp = digit_sum(num)
    if maxV < tmp:
        maxV = tmp
        ans = num

print(ans)
# nums = list(map(int, input().split()))

# for num in nums:
#     tmp_sum = 0



# maxV = 0
# for num in nums:
#     tmp = 0
#     for i in range(len(num)):
#         tmp += int(num[i])
#     if maxV < tmp:
#         maxV = tmp
#         ans = num
# print(ans)