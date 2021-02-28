# 거꾸로 출력 [::-1]
# tmp = 'asdf'
# print(tmp[::-1]) // result => fdsa

a = input()
tmp = []
tag = 0
for i in range(len(a)):
    if a[i] == '<' or tag == 1:
        tag = 1
        print(a[i], end="")
        if a[i] == '>':
            tag = 0 
    elif not tag:
        if a[i] == ' ':
            print(a[i], end='')
        else:
            tmp.insert(0, a[i])
        if i<len(a)-1:
            if a[i+1] == '<' or a[i+1] == ' ':
                for t in tmp:
                    print(t, end="")
                tmp = []
        elif i == len(a) - 1:
            for t in tmp:
                print(t, end="")
            tmp = []
