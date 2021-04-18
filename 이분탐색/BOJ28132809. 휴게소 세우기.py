import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
data = [0] + sorted(list(map(int, input().split())))

lt = 0
rt = L

while lt <= rt:
    mid = (lt+rt) // 2
    i = 0
    
