# D4
def check(cur, cur_sum):
    global ans
    if cur == N:
        if target <= cur_sum <= ans:
            ans = cur_sum
            return ans
    else:
        if selected[cur] == 0:
            selected[cur] = 1
            check(cur+1, cur_sum+heights[cur])
            selected[cur] = 0
            check(cur+1, cur_sum)
    return ans

for t in range(1, int(input())+1):
    N, target = map(int, input().split())
    heights = list(map(int, input().split()))
    selected = [0]*N
    ans = sum(heights)
    print('#%d %d' % (t, check(0,0)-target))
