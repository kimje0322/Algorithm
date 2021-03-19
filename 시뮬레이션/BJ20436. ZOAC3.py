def cal(dir,y,x):
    global prev_r, prev_l, time
    # 오른쪽
    if dir:
        # 첫번째 알파벳이면
        if not prev_r:
            time += abs(alp[sr][0]- y) + abs(alp[sr][1] - x)
            prev_r = (y, x)
        else:
            i, j = prev_r
            time += abs(i - y) + abs(j - x)
            prev_r = (y, x)
    # 왼쪽
    elif not dir:
        if not prev_l:
            time += abs(alp[sl][0] - y) + abs(alp[sl][1] - x)
            prev_l = (y, x)
        else:
            i, j = prev_l
            time += abs(i - y) + abs(j - x)
            prev_l = (y, x)

sl, sr = input().split()
word = input()
prev_r = ''
prev_l = ''
# 시간 차이 확인해보기(list직접 입력 vs list())
keybord = [list('qwertyuiop'),list('asdfghjkl'),list('zxcvbnm')]
right = list('yuiophjklbnm')
alp = dict()
for i in range(3):
    for j in range(len(keybord[i])):
        alp[keybord[i][j]] = (i,j)
time = 0
time += len(word)
for w in word:
    if w in right:
        if not prev_r and sr == w:
            prev_r = alp[w]
            continue
        cal(1,alp[w][0],alp[w][1])
    else:
        if not prev_l and sl == w:
            prev_l = alp[w]
            continue
        cal(0,alp[w][0],alp[w][1])
print(time)
