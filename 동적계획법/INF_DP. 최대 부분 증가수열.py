# 앞에서부터 data의 각 원소를 증가수열 마지막 원소라고 생각하고
# dy 리스트에 최대 개수를 저장
# 뒤로 이동하면서 data의 숫자가 더 작으면
# dy에 저장된 이전 최대 개수에 +1

def dp(n):
    ans = 0
    # 현재위치
    for i in range(n):
        # 앞 원소
        maxV = 0
        for j in range(i-1, -1, -1):
            if data[j] < data[i] and maxV < dy[j]:
                maxV = dy[j]
        dy[i] = maxV + 1
        if dy[i] > ans:
            ans = dy[i]
    return ans
N = int(input())
data = list(map(int, input().split()))
dy = [0]*N
print(dp(N))