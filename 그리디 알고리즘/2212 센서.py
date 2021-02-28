# 모범 답안
# 내 코드와 다른점
# 1. 내코드는 코드를 짜면서 생각나는대로 구현하는 느낌이라면
# 이 코드는 코드를 짜기전에 코드로 쉽게 나타낼 수 있는 풀이를 생각하고 구현한 느낌
# 2. 나도 그렇다면 코드 짜기 전에 명료한 풀이를 생각해내면 되는 것인데
# 그 풀이를 생각해내는 것이 참 쉽지 않다.
# k-1만큼 가장 먼 거리(distance.pop())를 빼고 나머지 distance원소의 합을 답으로 구현했다.
# 나는 평균값 구하고, 리스트를 슬라이싱으로 변형하는 등의 방법을 생각했는데
# 역시 답은 생각보다 참 간단하다..
# 그런 간단한 풀이가 왜 떠오르지 않을까.
# 그리디는 sort만 하고나면 대부분 간단한 로직 하나로(for문 하나라든지) 끝나는 듯
n = int(input())
k = int(input())
lst = list(map(int, input().split()))
lst.sort()
if k >= n:
    print(0)
else:
    distance = []
    for i in range(1, n):
        distance.append(lst[i] - lst[i-1])
    distance.sort(reverse=True)
    for _ in range(k-1):
        distance.pop(0)
    print(sum(distance))

# 내 답안(런타임에러)
# 차이가 같은 경우, 슬라이싱으로 이미 잘려나간 list를 참조하게 될 수 있어서 그런듯
# n = int(input())
# k = int(input())
# lst = list(map(int, input().split()))
# lst.sort()
# if k >= n:
#     print(0)
# else:
#     distance = []
#     for i in range(1, n):
#         distance.append((lst[i] - lst[i-1],lst[i-1]))
#     # 왜 sort가 내림차순으로 정렬된거지?;
#     # [(3, 3), (2, 7), (2, 1), (1, 6), (0, 6)]
#     distance.sort()
#     # distance.reverse()
#     ans = 0
#     for d in range(k-1):
#         idx = lst.index(distance.pop()[1])
#         tmp = lst[:idx+1]
#         ans += tmp[-1]-tmp[0]
#         lst = lst[idx+1:]
#     ans += lst[-1] - lst[0]
#     print(ans)