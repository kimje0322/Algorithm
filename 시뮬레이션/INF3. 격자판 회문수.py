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
    # 가로
    for i in range(7):
        for j in range(3):
            cur = ''
            for l in range(5):
                cur += board[i][j+l]
            if pal(cur):
                cnt += 1
    # 세로
    for j in range(7):
        for i in range(3):
            cur = ''
            for l in range(5):
                cur += board[i+l][j]
            if pal(cur):
                cnt += 1
make_word()
print(cnt)