from itertools import combinations

def solution(prices,d,k):
    prices.sort()
    answer = 0
    if prices[-1] - prices[0] <= d:
        answer = sum(prices) // len(prices)
    else:
        if prices[-2] - prices[1] <= d:
            prices.pop()
            prices.pop(0)
            answer = sum(prices) // len(prices)
        else:
            lst = list(combinations(prices,k))
            tmp = 999999
            flag = False
            for data in lst:
                if abs(data[-1]-data[0]) <= d:
                    flag = True
                    tmp = min((data[-1]+data[0])//2, tmp)
            if flag:
                answer = tmp
            else:
                n = len(prices)
                if n % 2:
                    answer = prices[n//2]
                else:
                    answer = prices[n//2-1]
    return answer


print(solution([1, 8, 1, 8, 1, 8],6,4))
