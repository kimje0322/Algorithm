n = int(input())
score = list(map(int, input().split()))
prev_right = 0
ans = 0
for s in score:
    if s == 1:
        prev_right += 1
        ans += prev_right
    else:
        prev_right = 0
print(ans)
