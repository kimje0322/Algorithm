import sys
input = sys.stdin.readline

N = int(input())
location = []
for _ in range(N):
    x,y = map(int, input().split())
    location.append((x,y))
location.sort()
# location.sort(key=lambda x:(x[0], x[1]))
for x,y in location:
    print(x,y)
