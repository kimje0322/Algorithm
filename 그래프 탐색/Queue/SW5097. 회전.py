for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    front = 0
    for i in range(M):
        front =(front+1) % N
    print('#%d %d' % (t, arr[front]))