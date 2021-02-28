n, l = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()
for i in heights:
    if i <= l:
        l += 1
print(l)

# if any([h <= l for h in heights]):
# l += 13 10
# 10 11 13
# heights.pop(heights.index(h)) // 여기서 h를 사용할 수 없어서 any쓰는 것을 포기함.

# 두번째 시도
# i = 0
# while True:
#     if all([h > l for h in heights]):
#         break
#     if l >= heights[i]:
#         l += 1
#         heights.pop(i)
#         i = 0
#     else:
#         i += 1
