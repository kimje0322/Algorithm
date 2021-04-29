# 돌다리 idx, 정답(word) idx, angle/devil
def move(f,c,r):
    global ans
    if f == len(word):
        ans += 1
        return
    # devil
    if r == 0:
        for i in range(c, len(devil)):
            print(word[f], devil[i])
            if word[f] == devil[i]:
                move(i+1, f+1, 1)
    # angel <= r:1
    else:
        for i in range(c, len(angel)):
            print(word[f], angel[i])
            if word[f] == angel[i]:
                move(i+1, f+1, 0)
    return

ans = 0
word = input()
devil = input()
angel = input()
n = len(angel)
move(0,0,0)

