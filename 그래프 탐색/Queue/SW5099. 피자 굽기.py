for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    queue = []
    # 화덕 크기만큼 피자 올리기
    for i in range(N):
        queue.append((cheese[i],i))
    # 대기하고 있는 최초 피자 index
    i = 0
    # 화덕에 피자가 있는 동안 반복
    while len(queue) != 1:
        # 맨 앞자리 피자 꺼내서 확인
        cur,idx = queue.pop(0)
        cur //= 2
        if cur:
            queue.append((cur,idx))
        else:
            # 새로 추가할 피자가 있으면
            if N+i < M:
                # 빠진 자리에 새롭게 피자 추가
                queue.append((cheese[N+i],N+i))
                i += 1

    print('#%d %d' % (t, queue[0][1]+1))
