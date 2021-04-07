board = [list(input().split()) for _ in range(7)]
# 회문 검사
cnt = 0
def pal(s):
    n = len(s)//2
    for i in range(n):
        if s[i] != s[-1-i]:
            return False
    return True

# 단어 완성
def make_word():
    global cnt
    # 강의 코드
    # 출발점을 큰 for 문에 쓴다.
    # for i in range(3):
    #     for j in range(7):
    #         tmp = board[j][i:i+5]
    #         pal(tmp)
    #

    for i in range(7):
        for j in range(3):
            cur1 = ''
            cur2 = ''
            for l in range(5):
                cur1 += board[i][j+l]
                cur2 += board[j+l][i]
            if pal(cur1):
                cnt += 1
            if pal(cur2):
                cnt += 1
make_word()
print(cnt)