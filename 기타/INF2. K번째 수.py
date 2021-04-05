for t in range(int(input())):
    N, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    res = [num[s-1]]
    for i in range(s, e):
        res.append(num[i])
    res.sort()
    print('#%d %d' % (t+1, res[k-1]))


    # 버블 정렬? 다시 공부하기
    # for i in range(len(res)-1):
    #     min_idx = 999999
    #     for j in range(i+1,len(res)):
    #         if min_idx > num[j]:
    #             min_idx = num[j]
    #     if num[i] > min_idx:
    #         num[i], min_idx =
    # res = sorted(res)