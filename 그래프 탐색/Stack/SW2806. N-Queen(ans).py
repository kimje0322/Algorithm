def possible(k, c): #k번 퀸의 위치는 (k,c)
    for r in range(k):
        if abs(k-r) == abs(c-queens[r]):
            return False
    return True

def nQueen(k):
    global cnt
    if k == N:
        cnt += 1
    else:
        for i in range(N):
            if visit[i]: continue
            # 퀀들이 대각에 위치하는지 판단
            # k번째 퀸 값을 i로 결정
            # 이전에 결정한 상태는 0 ~ k-1까지
            if not possible(k, i): continue
            visit[i] = 1
            queens[k] = i
            nQueen(k+1)
            # i를 다 돌았는데 새로운 queen을 만들지 못했으면
            # k와i를 돌려놓은 상태에서 visit를 초기화
            visit[i] = 0

for t in range(1, int(input())+1):
    N = int(input())
    queens = [0] * N
    visit = [0] * N
    cnt = 0
    nQueen(0)
    print('#%d %d' % (t, cnt))