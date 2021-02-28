k = int(input())
num = []
for i in range(k):
    n = int(input())
    if n != 0:
        num.append(n)
    elif n == 0:
        num.pop()
print(sum(num))

