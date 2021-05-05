import sys
input = sys.stdin.readline
# input 다음 줄에 공백줄 생김 => strip

n = input()
data = input().strip()
ans = 0
for x in data:
    ans += int(x)
print(ans)
