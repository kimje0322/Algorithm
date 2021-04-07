k, n = map(int, input().split())
line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt <= rt:
    mid = (lt+rt) // 2
    