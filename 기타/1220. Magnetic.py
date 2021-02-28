import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    num = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(100)]
    count = 0
    for i in range(num):
        tmp = []
        for j in range(num):
            # s극 1 // n극 2
            if magnetic[j][i]:
                tmp.append(magnetic[j][i])

        if tmp and tmp[0] == 2:
            tmp.pop(0)
        if tmp and tmp[-1] == 1:
            tmp.pop()

        for t in range(len(tmp)-1):
            if tmp[t] == 1 and tmp[t+1] == 2:
                count += 1

    print('#%d' %tc, count)