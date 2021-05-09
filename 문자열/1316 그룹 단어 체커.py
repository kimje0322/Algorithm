# 다른 풀이
# count = 0
# num = int(input())
#
# for i in range(num):
#     string = input()
#     if list(string) == sorted(string, key=string.find):
#         count += 1
#
# print(count)

# ans = n = int(input())
# for _ in range(n):
#     check = [0]*26
#     word = input()
#     check[ord(word[0])-97] = 1
#     for i in range(1, len(word)):
#         if word[i-1] == word[i]:
#             continue
#         elif check[ord(word[i])-97] == 0:
#             check[ord(word[i])-97] = 1
#         elif check[ord(word[i])-97] == 1:
#             ans -= 1
#             break
# print(ans)

import sys
input = sys.stdin.readline
# 람다
arr = [(28, "jy") , [60 , "bg"] , [51 , "ak"]]
arr.sort(key=lambda x:x[1])
print(arr)