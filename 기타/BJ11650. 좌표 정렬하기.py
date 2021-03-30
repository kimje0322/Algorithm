N = int(input())
location = []
for _ in range(N):
    x,y = map(int, input().split())
    location.append((x,y))
# location.sort()
location.sort(key=x[1])
print(location)
