# 생각보다 간단한 문제였다.
# 코드짜기 전에 일반식을 더 정성껏 짜야겠다.

n = int(input())
lst = []
ans = 0
for _ in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
for i in range(len(lst)):
    ans = max(ans, lst[i] * (i+1))
print(ans)
# if lst[0] <= n*lst[-1]:
#     ans = n*lst[-1]
# elif lst[0] > n*lst[-1]:
#     n = n-1
#     i = 1
#     tmp = 0
#     while i <= len(lst)-2:
#         for x in range(i+1):
#             tmp += lst[x]
#         ans = max(tmp // (i+1), ans)
#         tmp = 0
#         i += 1
# print(ans)
