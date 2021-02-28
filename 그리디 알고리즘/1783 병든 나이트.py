# 문제 해결 방법
# 변수 n과 m에 따라 답이 달라지지만
# 두 변수 중 기준 하나를 잡고 경우의 수를 촘촘하게 나누어서
# 일반식으로 답을 도출한다.

# n 세로 m 가로
n, m = map(int, input().split())
if n == 1:
    cnt = 1
elif n == 2:
    cnt = min(4, (m+1)//2)
elif n >= 3:
    if m <= 6:
        cnt = min(4, m)
    else:
        cnt = m - 2
print(cnt)