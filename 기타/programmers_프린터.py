from collections import deque

def solution(priorities, location):
    answer = 0
    max_p = max(priorities)
    while True:
        cur = priorities.pop(0)
        if max_p == cur:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1

