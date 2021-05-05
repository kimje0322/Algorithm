import sys
input = sys.stdin.readline

def func(file, target):
    i, cnt = 0, 0
    if len(file) >= len(target):
        while i <= len(file) - len(target):
            if file[i:i+len(target)] == target:
                cnt += 1
                i += len(target)
            else:
                i += 1
        return cnt
    else:
        return 0
f = input()
t = input()
print(func(f, t))

