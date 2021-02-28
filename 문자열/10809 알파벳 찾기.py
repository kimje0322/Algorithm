word = input()
check = [-1]*26
for w in range (len(word)):
    if check[ord(word[w]) - 97] == -1:
        check[ord(word[w]) - 97] = w
print(*check)
# ord(a) = 97 (0)
# ord(z) = 122 (25)
