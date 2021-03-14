N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
ans = [0]*M
selected = [0]*N
def backtracking(depth, N, M):
    if depth == M:
        print(' '.join(map(str, ans)))
        return
    overlap = 0
    for i in range(N):
        # 이번에 들어갈 원소가 직전 출력된 원소[-1]와 다르면
        if not selected[i] and overlap != num[i]:
            selected[i] = 1
            ans[depth] = num[i]
            # depth(i)가 바뀔 때 overlap도 새로 씌워짐
            overlap = num[i]
            backtracking(depth+1, N, M)
            selected[i] = 0
backtracking(0,N,M)


# def solve(depth, N, M):
#     if depth == M:
#         print(' '.join(map(str, ans)))
#         return
#     overlap = 0
#     for i in range(N):
#         if not selected[i] and overlap != num[i]:
#             selected[i] = 1
#             ans.append(num[i])
#             overlap = num[i]
#             solve(depth+1, N, M)
#             selected[i] = 0
#             ans.pop ()
# solve(0,N,M)
