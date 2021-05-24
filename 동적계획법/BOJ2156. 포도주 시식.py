n = int(input())
wine = []
for _ in range(n):
    wine.append(input())
dp = [wine[0], wine[0]+wine[1]]+[0]*(n-2)

for i in range(3,n+1):
    pass