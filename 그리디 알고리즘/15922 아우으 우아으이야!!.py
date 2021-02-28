# 뭐 때문에 시간이 오래 걸렸나, 잘 안풀렸나?
# 1) 경우의 수를 나눌 때, 빠진 경우가 있어서 히든 테케에서 걸린 것 같다.
# 2) 경우의 수를 보다 간소하게 나누는 것이 좋을 것 같다.
# 3) 꼭 리스트에 담지 않아도, 매번 인풋을 받으면서 비교하는 방법도 고려해보자.
n = int(input())
l = list()
for _ in range(n):
    x, y = map(int, input().split())
    l.append((x,y))
ans = 0
cur_x = l[0][0]
cur_y = l[0][1]
for i in range(1, len(l)):
    if cur_x == l[i][0]:
        cur_y = l[i][1]
    elif l[i][0] < cur_y < l[i][1]:
        cur_y = l[i][1]
    elif l[i][0] >= cur_y:
        ans += abs(cur_y - cur_x)
        cur_x = l[i][0]
        cur_y = l[i][1]
ans += abs(cur_y - cur_x)
print(ans)



# 테케는 맞았는데 어떤 상황에서 틀린 지 잘 모르겠음.
# for i in range(len(l)):
#     if i >= 1 and l[i-1][1] > l[i][0]:
#         # 부분 덮임
#         if l[i-1][1] < l[i][1]:
#             ans += abs(l[i][1] - l[i-1][1])
#         # 아예 덮임
#         if l[i-1][1] >= l[i][1]:
#             pass
#     # 겹치는 부분 없음
#     elif i == 0 or (i >= 1 and l[i-1][1] <= l[i][0]):
#         ans += abs(l[i][1] - l[i][0])
