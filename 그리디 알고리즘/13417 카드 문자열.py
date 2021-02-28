for t in range(int(input())):
    n = int(input())
    alp = list(input().split())
    ans = [alp[0]]
    for i in range(1, len(alp)):
        if ord(alp[i]) <= ord(ans[0]):
            ans.insert(0, alp[i])
        elif ord(alp[i]) >= ord(ans[0]):
            ans.append(alp[i])
    for w in ans:
        print(w, end="")
    print()