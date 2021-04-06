n, m = map(int,input().split())
A = list(map(int, input().split()))
lt = 0
rt = 1
tot = A[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += A[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= A[lt]
        lt += 1
    else:
        tot -= A[lt]
        lt += 1

print(cnt)