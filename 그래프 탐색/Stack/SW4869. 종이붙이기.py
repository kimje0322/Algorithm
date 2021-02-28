def f(n):
    if n < 2:
        return 1
    else:
        return f(n-1) + 2*f(n-2)

for t in range(1, int(input())+1):
    n = int(input()) // 10
    print('#%d %d' % (t, f(n)))
