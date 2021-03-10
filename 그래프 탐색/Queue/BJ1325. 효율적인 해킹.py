# 속도 개선을 위해 할 것
# 1. input()보다는 sys.stdin.readline
# 2. 빈 리스트에 append 하는 것 보다는 입력 받을 개수 만큼 리스트 초기화하고 인덱스로 접근하여 입력하기
# 3. 줄바꿈할 때 매번 print() 보다는 문자열 변수에 += 저장해서 한번에 출력하기
# 4. queue 직접 구현하지 않고 import collections 으로 deque 사용

# 시간 초과로 인해 코드 수정을 여러번 반복했다.
# pypy3로 제출하여 통과했다.
# 백준에서도 python으로 통과한 사람은 3명밖에 없는 것으로 보아
# 파이썬으로 시간초과없이 해결하기엔 다소 힘든 문제인 것 같다.

import sys
input = sys.stdin.readline
from collections import deque

def bfs(idx):
    d = 0
    queue = deque()
    queue.append(idx)
    while queue:
        cur = queue.popleft()
        d += 1
        for next_node in adj[cur]:
            if not visited[next_node]:
                visited[next_node] = 1
                queue.append(next_node)
    return d

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
ans = []
maxV = 0
for _ in range(M):
    a, b = map(int, input().split())
    adj[b].append(a)
for i in range(1, N+1):
    if adj[i]:
        visited = [0] * (N + 1)
        visited[i] = 1
        tmp = bfs(i)
        if maxV <= tmp:
            if maxV < tmp:
                ans = []
            maxV = tmp
            ans.append(i)

print(*ans)
# print(*[i for i, ele in enumerate(ans) if ele == max(ans)])

