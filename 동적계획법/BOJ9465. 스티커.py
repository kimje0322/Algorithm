for _ in range(int(input())):
    n = int(input())

    li = []
    for _ in range(2):
        li.append(list(map(int, input().split())))

    li[0][1] += li[1][0]
    li[1][1] += li[0][0]

    for j in range(2, n):
        li[0][j] += max(li[1][j - 1], li[1][j - 2])
        li[1][j] += max(li[0][j - 1], li[0][j - 2])

    ans = max(li[0][n - 1], li[1][n - 1])
    print(ans)