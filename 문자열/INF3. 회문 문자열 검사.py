# if word == word[::-1] => 회문
def check_palindrome(word):
    N = len(word)
    for i in range(N//2):
        if word[i] != word[-1-i]:
        # if word[i] != word[N-i-1]:
            return 'NO'
    return 'YES'

n = int(input())
for t in range(n):
    print('#%d %s' %(t+1, check_palindrome(input().lower())))