# 새롭게 안 지식
# eval
# python 의 built-in 함수 중 하나인 eval 함수는 매우 강력하면서도 사용을 자제 하도록 권고하는 양날의 검과 같은 기능이다.
# eval 함수는 expression 인자에 string 값을 넣으면 해당 값을 그대로 실행하여 결과를 출력해 준다
# eval("(5 * 10) / 2")
# >>> 25
# 위험한 이유
# 1. 서버 root 디렉토리 정보가 그대로 노출될 수 있다.
# 2. 코드의 가독성을 떨어뜨리고 디버깅을 어렵게 만들 수 있다.
# 3. eval을 사용해 일부 로컬 환경에 의존하도록 구현할 경우 환경 의존성도 생길 수 있다.

n, k  = map(int, input().split())
lst = []
for coin in range(n):
    lst.append(int(input()))
lst.reverse()
ans, i = 0, 0
while True:
    if k >= lst[i]:
        ans += k//lst[i]
        if k % lst[i]:
            k = k % lst[i]
        elif not k % lst[i]:
            break
    if i < len(lst):
        i += 1
print(ans)
