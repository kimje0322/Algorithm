queue = []
snack = 20
queue.append((1, 0))  # 1번 줄서기
i = 1
while snack>0:
    x, y = queue.pop(0)  # 마이쭈 받는다
    snack -= y + 1
    #마이쭈 받기, 다시 줄 서기
    i += 1
    queue.append((x, y + 1))  # 다시 줄 서기
    queue.append((i,0))
    last = x
print(last)

