# 개행문자 처리
import sys
import copy
input = sys.stdin.readline
R, C = map(int, input().split())
# data = [['.' for _ in range(C+2)]]+[['.']+list(input())+['.'] for _ in range(R)] + [['.' for _ in range(C+2)]]
data = [list('.'*(C+2))]
for _ in range(R):
    data.append(['.']+list(input().strip())+['.'])
data.append(list('.'*(C+2)))
print(data)
new_map = copy.deepcopy(data)
direction = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(1,R+1):
    for j in range(1,C+1):
        if data[i][j] == 'X':
            cnt = 0
            for y,x in direction:
                ny, nx = i+y, j+x
                if 0 <= ny < R+2 and 0 <= nx < C+2 and data[ny][nx] == '.':
                    cnt += 1
                if cnt >= 3:
                    new_map[i][j] = '.'
                    break
# 윗면, 아랫면 삭제
new_map = new_map[1:len(new_map)-1]
# print(new_map)
xlst, ylst = [], []
for i in range(len(new_map)):
    for j in range(len(new_map[0])):
        if new_map[i][j] == 'X':
            xlst.append(j)
            ylst.append(i)
# print('-----')
for ele in new_map[min(ylst):max(ylst)+1]:
    print(''.join(ele[min(xlst):max(xlst)+1]))




# 6 4
# .X..
# XXX.
# ...X
# ...X
# XX.X
# ...X