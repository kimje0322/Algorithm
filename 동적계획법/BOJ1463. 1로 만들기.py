def f(n):
    cnt = 0
    while True:
        if not n % 3:
            n //= 3
            cnt += 1
            if n == 1:
                return cnt
        if not n % 2:
            n //= 2
            cnt += 1
            if n == 1:
                return cnt
        n -= 1
        cnt += 1
        if n == 1:
            return cnt

    return cnt
num = int(input())
print(f(num))