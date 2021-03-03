def check(idx, sum_num):
    global ans
    if sum_num >= ans:
        return
    if idx == N:
        if sum_num >= target:
            ans = sum_num
            # 여기서 아예 함수 종료하면 시간 단출될텐데...
            return
    else:
        selected[idx] = 1
        check(idx+1, sum_num+heights[idx])
        selected[idx] = 0
        check(idx+1, sum_num)

for t in range(1, int(input())+1):
    N, target = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort()
    ans = sum(heights)
    selected = [0]*N
    check(0,0)
    print('#%d %d' % (t, ans-target))
