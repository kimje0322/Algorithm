def find(alp, dir):
    for i in range(3):
        for j in range(len(keybord[i])):
            if keybord[i][j] == alp:
                cal(dir, i,j)

def cal(dir,y,x):
    global prev_r, prev_l, time
    # 오른쪽
    if dir:
        # 첫번째 알파벳이면
        if not prev_r:
            prev_r = (y, x)
        else:
            i, j = prev_r
            time += abs(i) - y) + abs(j - x)
            prev_r = (y,x
    # 왼쪽
    elif not dir:
        if not prev_l:
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
left = list('yuiophjklbnm')
time = 0
time += len(word)
for w in word:
    if w in left:

        find(w,0)
    else:
        find(w,1)
print(time)
