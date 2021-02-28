def check_str(a,b):
    minimum = 50
    for i in range(len(b) - len(a) + 1):
        cnt = 0
        for j in range(len(a)):
            if a[j] != b[i+j]:
                cnt += 1
        if minimum > cnt:
            minimum = cnt
    print(minimum)
    # ans = 0
    # if len(a) == len(b):
    #     for i in range(len(a)):
    #         if a[i] == b[i]:
    #             ans += 1
    # elif a in b:
    #     ans = 0
    # else:
    #     tmp = 0
    #     i = 0
    #     for j in range(len(b)-len(a)):
    #         while i < len(b):
    #             if a[i+j] == b[i]:
    #                 tmp += 1
    #             i += 1
    #
    # print(ans)
a, b = input().split()
check_str(a,b)
