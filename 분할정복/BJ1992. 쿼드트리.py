import sys
input = sys.stdin.readline
# 단일 구성 확인(단일구성이면 return True)

def divide(n, y, x):
    global ans
    zero, one = 0, 0
    # 사작점 좌표 + 크기(n)
    for i in range(y, y + n):
        for j in range(x, x + n):
            if zero and one:
                break
            if board[i][j] == '0':
                zero = 1
            elif board[i][j] == '1':
                one = 1
    # 0,1 둘 중 하나로 구성되면
    if zero != one:
        if zero:
            ans += '0'
        elif one:
            ans += '1'
    # 섞여있으면 다시 나누기
    else:
        small_n = n // 2
        ans += '('
        divide(small_n, y, x)
        divide(small_n, y, x + small_n)
        divide(small_n, y + small_n, x)
        divide(small_n, y + small_n, x + small_n)
        ans += ')'

N = int(input())
board = [input() for _ in range(N)]
ans = ''
divide(N,0,0)
print(ans)




# def check(n, y, x):
#     global ans
#     zero = 0
#     one = 0
#     for i in range(y, y + n):
#         for j in range(x, x + n):
#             if zero and one:
#                 divide(n, y, x)
#                 return
#
#             if board[i][j] == '0':
#                 zero = 1
#             elif board[i][j] == '1':
#                 one = 1
#     if zero:
#         ans += '0'
#         return
#     elif one:
#         ans += '1'
#         return
#
#
# def divide(n, y, x):
#     global ans
#     small_n = n//2
#     ans += '('
#     check(small_n, y, x)
#     check(small_n, y, x + small_n)
#     check(small_n, y + small_n, x)
#     check(small_n, y + small_n, x + small_n)
#     ans += ')'
#     return
#
# N = int(input())
# board = [input() for _ in range(N)]
# ans = ''
# divide(N,0,0)
# print(ans)