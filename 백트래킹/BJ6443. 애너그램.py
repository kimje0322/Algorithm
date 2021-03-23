# N개의 영단어에 대한 모든 가능한 애너그램을 출력한다.
# 각각의 영단어에 대한 애너그램을 출력할 때, 알파벳 순서로 중복되지 않게 출력한다.
import sys
input = sys.stdin.readline

def perm(idx):
    global ans
    n = len(alp)
    if idx == n:
        answer.append(ans)
        return
    # 이전 요소와 겹쳤는지 확인
    overlap = 'none'
    for i in range(n):
        if not selected[i] and overlap != alp[i]:
            selected[i] = 1
            ans += alp[i]
            overlap = alp[i]
            perm(idx+1)
            selected[i] = 0
            ans = ans[:len(ans)-1]
    return

N = int(input())
for _ in range(N):
    # alp변수를 순열을 만들기 쉽게 sort
    alp = sorted(input())
    # 해당 알파벳이 사용되었는지 여부 / alp의 인덱스를 같이 씀
    selected = [0]*len(alp)
    ans = ''
    answer = []
    perm(0)
    for x in answer:
        print(x)
