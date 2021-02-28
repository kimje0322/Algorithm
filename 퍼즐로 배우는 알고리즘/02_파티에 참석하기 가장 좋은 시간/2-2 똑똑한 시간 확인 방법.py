# tlist = [(5,0),(2,0),(11,0),(8,0),(1,0)]

sched2 = [(6.0,8.0), (6.5, 12.0), (6.5, 7.0),
          (7.0, 8.0), (7.5, 10.0), (8.0,9.0)]

def bestTime(schedule):
    times = []
    for c in schedule:
        times.append((c[0], 'start'))
        times.append((c[1], 'end'))
    sortList(times)
    maxcount, time =chooseTime(times)
    print('Best time to attend the party is at', time, ':', maxcount, 'will be attending!')

def sortList(tlist):
    for i in range(len(tlist)-1):
        iSm = i
        for j in range(i, len(tlist)):
            if tlist[iSm][0] > tlist[j][0]:
                iSm = j
        tlist[i], tlist[iSm] = tlist[iSm], tlist[i]

# times 각 연예인들의 시작 시간
def chooseTime(times):
    rcount = 0
    maxcount = time = 0
    for t in times:
        if t[1] == 'start':
            rcount = rcount + 1
        elif t[1] == 'end':
            rcount = rcount - 1
        if rcount > maxcount:
            maxcount = rcount
            time = t[0]
    return maxcount, time

bestTime(sched2)