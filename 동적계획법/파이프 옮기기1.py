N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
stack = []
data[0][0], data[0][1] = 3, 3
stack.append((0,1))
# 0가로, 1세로, 2대각선
# direction = [(0,1),(1,0),(1,1)]
dx, dy = [1,0,1],[0,1,1]
prev = (0,0)
while stack:
    x,y = stack.pop()
    for d in range(3):
        if (x+dx[d], y+dy[d]) == prev:
            dir = ds
            break
    # 가로
    if dir == 0:
        pass

        stack.append()
# 이전노드와 현재노드가 어떤 모양인지 확인(가로, 세로, 대각선)
# 각 모양별로 가능한 다음 노드 stack에 넣기
# bfs
