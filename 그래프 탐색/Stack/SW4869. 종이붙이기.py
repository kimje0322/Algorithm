def f(n):
    if n < 2:
        return 1
    else:
        return f(n-1) + 2*f(n-2)

for t in range(1, int(input())+1):
    n = int(input()) // 10
    print('#%d %d' % (t, f(n)))

# 복습 코드
# def f(num):
#     if num == 1:
#         return 1
#     elif num == 2:
#         return 3
#     else:
#         return f(num-1) + 2*f(num-2)
#
# for t in range(1, int(input())+1):
#     n = int(input())//10
#     print('#%d %d' % (t, f(n)))
