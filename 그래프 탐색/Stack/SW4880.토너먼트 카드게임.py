# 목표 2:45
def win(a, b):
    if card[a] == card[b]:
        return min(a,b)
    # 홀수
    if (card[a]+card[b]) % 2:
        if card[a] > card[b]:
            return a
        else:
            return b
    # 짝수
    else:
        if card[a] < card[b]:
            return a
        else:
            return b

def match(start, end):
    if start == end:
        return start
    else:
        center = (start+end)//2
        first = match(start, center)
        second = match(center+1, end)
        return win(first, second)


for t in range(1, int(input())+1):
    N = int(input())
    card = [0]+list(map(int, input().split()))
    start = 1
    end = N
    print('#%d %d' % (t, match(1, N)))



# 어려웠던 부분
# first와 second값이 각각 return 되어 구해진 뒤, 그 값들이 다시 first값으로 채워지는 흐름

# card = [idx for idx in enumerate(input().split())]
# card = [(idx+1, int(rcp)) for idx, rcp in enumerate(input().split())]