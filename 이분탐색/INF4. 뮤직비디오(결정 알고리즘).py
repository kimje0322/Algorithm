def Count(capacity):
    cnt = 1
    sum = 0
    for x in data:
        if sum+x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt
n, m = map(int, input().split())
data = list(map(int, input().split()))
lt = 1
rt = sum(data)
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid)<=m:
        ans = mid
        rt = mid - 1
    else:
        lt = mid+1
print(ans)



# while lt <= rt:
#     mid = (lt+rt) // 2
#     tmp, i = 0, 0
#     while tmp < mid:
#         tmp += data[i]
#     cnt += 1
#     lt = i
#     if cnt == m:
#         break
# print()