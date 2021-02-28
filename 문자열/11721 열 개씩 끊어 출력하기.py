word = input()
cnt = 0
for i in range(len(word)):
    print(word[i], end='')
    cnt += 1
    if cnt == 10:
        print()
        cnt = 0

# s = input()
# while s:
#     print(s[:10]);
#     s=s[10:]