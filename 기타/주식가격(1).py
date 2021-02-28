import collections 

def solution(prices):
    answer = []
    prices = collections.deque(prices)
    while prices:
        c = prices.popleft()
        
        cnt = 0
        for i in prices:
            if c > i:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    return answer
                
                
  