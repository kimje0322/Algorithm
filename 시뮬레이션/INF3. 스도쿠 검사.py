def check_rc():
    for i in range(9):
        cnt_r = [0] * 10
        cnt_c = [0] * 10
        for j in range(9):
            if not cnt_r[sudoku[i][j]]:
                cnt_r[sudoku[i][j]] += 1
            else:
                return False
            if not cnt_c[sudoku[j][i]]:
                cnt_c[sudoku[j][i]] += 1
            else:
                return False
    return True

def check_rec():
    # 강의 코드
    for i in range(3):
        for j in range(3):
            cnt = [0]*10
            for k in range(3):
                for s in range(3):
                    if not cnt[sudoku[i*3+k][j*3+s]]:
                        cnt[sudoku[i*3+k][j*3+s]] += 1
                    else:
                        return False
    # for i in range(0,7,3):
    #     for j in range(0,7,3):
    #         cnt = [0] * 10
    #         for l in range(i, i+3):
    #             for k in range(j, j+3):
    #                 if not cnt[sudoku[l][k]]:
    #                     cnt[sudoku[l][k]] += 1
    #                 else:
    #                     return False
    return True
sudoku = [list(map(int, input().split())) for _ in range(9)]
if check_rc() and check_rec():
    print('YES')
else:
    print('NO')