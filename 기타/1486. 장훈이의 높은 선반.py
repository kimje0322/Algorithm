def power_set(n,k,s):
    if s >= B:
        return s
    else:
        selected[k] = 1
        power_set(n, k+1, s+heights[k])
        selected[k] = 0
        power_set(n,k+1,s)

for t in range(int(input())+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    selected = [0]*N
    print('#%d' % t, power_set(N,0,0) - B)