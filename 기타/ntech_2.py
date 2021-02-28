def solution(board):
    answer = -1
    white = check(board, 2)
    black = check(board, 1)
    if white and not black:
        answer = 2
    elif not white and black:
        answer = 1
    else:
        answer = 0
    return answer

def check(arr, flag):
    for i in range(15):
        for j in range(15):
            if arr[i][j] == flag:
                # 가로세기
                if i==0 or (i >= 1 and arr[i-1][j] != flag):
                    ni = i
                    nj = j
                    count = 0
                    while ni < 15 and nj <15:
                        if arr[ni][nj] == flag:
                            count += 1
                            ni = ni+1
                            nj = nj
                        else:
                            break
                    if count == 5:
                        return True
                # 세로 세기
                if j==0 or (j >= 1 and arr[i][j-1] != flag):
                    ni, nj = i, j
                    count = 0
                    while ni < 15 and nj < 15:
                        if arr[ni][nj] == flag:
                            count += 1
                            ni = ni
                            nj = nj + 1
                        else:
                            break
                    if count == 5:
                        return True
                # 대각선 세기
                if (i==0 and j==0) or (i>=1 and j>=1 and arr[i-1][j-1] != flag):
                    ni, nj = i, j
                    count = 0
                    while ni < 15 and nj < 15:
                        if arr[ni][nj] == flag:
                            count += 1
                            ni = ni+1;
                            nj = nj+1;
                        else:
                            break
                    if count == 5:
                        return True
                if (i==0 and j==0) or (i>=1 and j>=1 and arr[i-1][j-1] != flag):
                    ni, nj = i, j
                    count = 0
                    while ni < 15 and nj < 15:
                        if arr[ni][nj] == flag:
                            count += 1
                            ni = ni+1;
                            nj = nj-1;
                        else:
                            break
                    if count == 5:
                        return True

    return False



