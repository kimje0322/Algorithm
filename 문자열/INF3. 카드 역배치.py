card = [0]*21
for i in range(21):
    card[i] = i
for _ in range(10):
    a, b = map(int, input().split())
    size = (b - a)//2
    for i in range(size+1):
        card[a+i], card[b-i] = card[b-i], card[a+i]
    # for s in range(a, a+size+1):
        # card[s], card[a+b-s] = card[a+b-s], card[s]
card.pop(0)
print(*card)

