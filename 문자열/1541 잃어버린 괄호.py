n = input().split('-')
for i in range(len(n)):
    if '+' in n[i]:
        n[i] = sum(map(int, n[i].split('+')))
    else:
        n[i] = int(n[i])
print(n[0]-sum(n[1:]))