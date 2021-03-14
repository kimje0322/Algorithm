from itertools import combinations
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
for i in range(1,N+1):
    for x in combinations(data, i):
        if sum(x) == S:
            cnt += 1
print(cnt)

