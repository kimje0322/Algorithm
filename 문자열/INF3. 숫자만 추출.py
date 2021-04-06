string = input()
num = 0
for s in string:
    if 48 <= ord(s) <= 57:
        tmp = int(s)
        num = num*10 + tmp
num = int(num)
print(num)
cnt = 0
for i in range(1,num+1):
    if not num % i:
        cnt += 1
print(cnt)