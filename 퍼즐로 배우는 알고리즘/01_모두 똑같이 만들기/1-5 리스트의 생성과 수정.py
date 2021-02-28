# 결론
# 1. 리스트를 연결해서 합쳐주는 연산자 +는 새로운 리스트를 만들어서 그 결과를 저장한다.
# 2. 반면, append는 기존의 리스트를 수정한다.

def listConcatenate(caps):
    caps = caps + ['END']
    print(caps)

capA = ['F', 'F', 'B']
listConcatenate(capA)
print(capA)

# 결과
# ['F', 'F', 'B', 'END']
# ['F', 'F', 'B']

def listAppend(caps):
    caps.append('END')
    print(caps)

capA = ['F', 'F', 'B']
listAppend(capA)
print(capA)

# 결과
# ['F', 'F', 'B', 'END']
# ['F', 'F', 'B', 'END']
