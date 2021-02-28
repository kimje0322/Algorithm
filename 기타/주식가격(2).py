from collections import deque

def solution(prices):
    answer = []*len(prices)
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            elif prices[i] > prices[j]:
                cnt += 1
                break
        answer.append(cnt)
    answer.append(0)
    return answer