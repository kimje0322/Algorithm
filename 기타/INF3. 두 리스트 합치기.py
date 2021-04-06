n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))
ans = []
p1, p2 = 0, 0
while True:
    if p1 == n:
        ans += lst2[p2:]
        break
    elif p2 == m:
        ans += lst1[p1:]
        break
    if lst1[p1] <= lst2[p2]:
        ans.append(lst1[p1])
        p1 += 1
    elif lst1[p1] > lst2[p2]:
        ans.append(lst2[p2])
        p2 += 1

# for i in range(n):
#     j = -1
#     while j < m+n:
#         j += 1
#         if i == 0 and lst1[i] < lst2[j]:
#             lst2.insert(j,lst1[0])
#             break
#         elif lst1[i] <= lst2[j]:
#             lst2.insert(j, lst1[i])
#             break
#         if j == len(lst2)-1:
#             lst2.append(lst1[i])
#             break
print(*ans)
