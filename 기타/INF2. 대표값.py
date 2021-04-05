# round함수는 round_half_even 방식을 택한다.
# 사사오입 원칙
# 반올림할 자리의 수가 5이면 반올림 할 때
# 앞자리의 숫자가 짝수면 내림, 홀수면 올림 한다.
# round(4.5) // 4 (짝수->내림)
# round(3.5) // 4 (홀수->올림)

n = int(input())
score = list(map(int, input().split()))
avarage = round(sum(score)/n)
ans = []
min = 2147000000
for idx, x in enumerate(score):
    tmp = abs(avarage - score[idx])
    if tmp < min:
        min = tmp
        tmp_score = x
        res = idx + 1
    elif tmp == min:
        if x > tmp_score:
            tmp_score = x
            res = idx + 1

print(avarage, res)