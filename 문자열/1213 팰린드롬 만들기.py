def check_palindrome(word):
    cnt = 0
    ans = [0]*len(word)
    cnt_word = []
    one_word = list(set(word))
    one_word.sort()
    for i in range(len(one_word)):
        cnt_word.append(word.count(one_word[i]))
    for c in range(len(cnt_word)):
        if (cnt_word[c] % 2):
            cnt += 1
            ans[len(ans)//2] = word.pop(word.index(one_word[c]))
            if cnt >= 2:
                print("I'm Sorry Hansoo")
                return
    i = 0
    while word:
        if word[0] == word[1]:
            ans[i] = word.pop(0)
            ans[len(ans)-1-i] = word.pop(0)
        i += 1
    for w in ans:
        print(w, end='')

s = list(input())
s.sort()
check_palindrome(s)

