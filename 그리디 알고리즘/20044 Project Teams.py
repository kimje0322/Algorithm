n = int(input())
sw = list(map(int, input().split()))
sw.sort()
ans = list()
for i in range(len(sw)//2):
    ans.append(sw[i]+sw[-1-i])
print(min(ans))

# arr =[5,0,4]
# for i in range(len(arr)):
#     # print(arr[i])
#     print(~i)
#     // -1
#        -2
#        -3
