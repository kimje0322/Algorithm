t = int(input())
for tc in range(t):
    j, n = map(int, input().split())
    lst = []
    for _ in range(n):
        a, b = map(int, input().split())
        lst.append(a*b)
    lst.sort()
    num = 0
    for i in lst:
        if j <= 0:
            break
        if j <= i:
            num += 1
            break
        j -= i
        num += 1
    print(num)

# 선택정렬
# lst = [5,1,55,3,70]
# for i in range(len(lst)-1):
#     min_idx = i
#     for j in range(i+1, len(lst)):
#         if lst[j] < lst[min_idx]:
#             min_idx = j
#     lst[min_idx], lst[i] = lst[i], lst[min_idx]
# print(lst)