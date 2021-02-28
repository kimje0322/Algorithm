for t in range(1, int(input())+1):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]
    step = 0
    mid = N // 2
    sum_num = 0
    for i in range(N):
        for j in range(mid-step, mid+step+1):
            sum_num += farm[i][j]
        if i < N // 2:
            step += 1
        else:
            step -= 1

    print("#%d" % t, sum_num)

# for t in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, list(input()))) for _ in range(N)]
#
#     s = e = N//2
#     ans = 0
#     for row in range(N):
#         for i in range(s, e + 1):
#             ans += arr[row][i]
#
#         if row < N // 2:
#             s, e = s - 1,  e + 1
#         else:
#             s, e = s + 1, e - 1
#     print('#%d %d' % (t, ans))




