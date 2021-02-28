B = [[0,0,1,0],[1,0,0,0],[0,0,0,1],[0,1,0,0]]

# qindex: current 열에 있는 퀸의 행의 위치값
# current: 현재 열

#  인자로 열, 행을 따로 받는게 시작 위치값이 그때그때 달라지는 건가?
#  부분 설정된 체스판도 있어서?
def noConflicts(board, current, qindex, n):
    for j in range(current):
        if board[qindex][j] == 1:
            return False
    k = 1
    while qindex - k >= 0 and current - k >= 0:
        if board[qindex - k][current - k] == 1:
            return False
        k += 1
    k = 1
    while qindex + k < n and current - k >= 0:
        if board[qindex + k][current - k] == 1:
            return False
        k += 1
    return True


# def checkQueen(lst):
#     check_r = 0
#     check_c = 0
#
#     for i in range(len(B)):
#         for j in range(len(B[0])):
#             check_r += B[i][j]
#             check_c += B[j][i]
#         if check_c > 1 or check_r > 1:
#             return False
#         check_c, check_r = 0, 0
#     return True
#
#
# print(checkQueen(B))