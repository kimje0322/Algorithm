# 목표: 7시 20분
def calculate(cal_lst):
    stack = []
    for idx in range(len(cal_lst)):
       if cal_lst[idx] in operator:
           if len(stack) >= 2:
                a = int(stack.pop())
                b = int(stack.pop())
                if cal_lst[idx] == '+':
                    stack.append(b+a)
                elif cal_lst[idx] == '-':
                    stack.append(b-a)
                elif cal_lst[idx] == '*':
                    stack.append(b*a)
                else:
                    stack.append((b//a))
           else:
               return 'error'
       elif cal_lst[idx] == '.':
           return stack.pop()
       else:
           stack.append(int(cal_lst[idx]))

for t in range(1, int(input())+1):
    cal = input().split()
    operator = ['+', '-', '*', '/']
    operators = 0
    numbers = 0
    # 반복문 여기서 한번, 함수 돌리면서 한번
    # 총 두번 돌아가는데
    # 한 번만 돌릴 수 있는 방법 없을까
    for i in cal:
        if i in operator:
            operators += 1
        elif i != '.':
            numbers += 1
    if operators != numbers-1:
        print('#%d' %t, 'error')
    else:
        print('#%d' %t , calculate(cal))