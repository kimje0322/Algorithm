# n, m = map(int, input().split())
# n_lst = []
# cnt = 0
# for _ in range(n):
#     n_lst.append(input())
# for i in range(m):
#     a = input()
#     if a in n_lst:
#         cnt += 1
# print(cnt)

n, m = map(int, input().split())
c, r = [input() for i in range(n)], 0
for i in range(m):
    r += int(input() in c)
print(r)