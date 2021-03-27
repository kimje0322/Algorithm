ans = []
# 단일 구성 확인(단일구성이면 return True)
def check(r,c,y,x):
    global ans
    zero = 0
    one = 0
    for i in range(r,y):
        for j in range(c,x):
            if zero and one:
                divide(center//2,center-1)
                return

            if board[i][j] == '0':
                zero = 1
            elif board[i][j] == '1':
                one = 1
    if zero:
        ans.append('0')
        return 'zero'
    elif one:
        ans.append('1')
        return 'one'

def divide(center, n):
    # r c y x
    check(0,center-1,center-1,center-1)
    check(0,center,center,n)
    check(center,0,n,center-1)
    check(center,center,n,n)
    return

N = int(input())
board = [input() for _ in range(N)]
center = N//2
divide(center, N-1)
print(board)
# if check(0,0) == 'zero':
#     ans = 0
# elif check(0,0) == 'one':
#     ans = 1

