# 내 코드와 모범답안이 다른점
# 1. list를 두 개 따로 만들지 않음
# => 리스트를 따로 구현하는 문제가 아님. 차의 최댓값만 구하면 되었다.
# 2. 대신 인덱스 차이 2가 난다는 것을 이용해서 반복문 하나로 답을 구함
# 개선점
# 1. 숲을 보는 연습하기

# 모범 답안
# T=int(input())
# for i in range(T):
#     N=int(input())
#     trees=list(map(int,input().split()))
#     trees.sort()
#     result=0
#     for j in range(2, N):
#         result=max(result,abs(trees[j]-trees[j-2]))
#     print(result)

for t in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    even_ans = []
    odd_ans = []
    for i in range(len(lst)):
        # 홀수 인덱스
        if i%2:
            odd_ans.insert(0, lst[i])
        # 짝수 인덱스
        elif not i%2:
            even_ans.append(lst[i])
    ans = even_ans+odd_ans
    maximum = 0
    for x in range(1, len(ans)):
        maximum = max(abs(ans[x] - ans[x-1]), maximum)
    maximum = max(abs(ans[-1] - ans[0]), maximum)
    print(maximum)

