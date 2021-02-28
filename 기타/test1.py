# def cal(str):
instr = "20+33*4-75*2+3"
cal = []
cur = 0
# if '*' in str:
#     mul_stack.append(str.index('*'))
for i in range(len(instr)):
    if instr[i] == '+' or instr[i] == '-' or instr[i] == '*':
        cal.append(int(instr[cur:i]))
        cal.append(instr[i])
        cur = i + 1
cal.append(int(instr[cur:]))


i = 1
a = [1,3,4,6]

# a.remove(3)
# 인덱스, 추가할 숫자
# a.insert(0, 9)
# print(a)

while len(cal) != 0:
    if cal[i] == '*':
        tmp = cal[i-1] * cal[i+1]
        cal.remove(cal[i-1])
        cal.remove(cal[i-1])
        cal.remove(cal[i-1])
        cal.insert(i-1, tmp)
        i = i-1
    elif i < len(cal) - 1:
        i += 1
    else:
        break
i = 1
while True:
    if cal[i] == '+':
        tmp = cal[i-1] + cal[i+1]
        cal.remove(cal[i - 1])
        cal.remove(cal[i - 1])
        cal.remove(cal[i - 1])
        cal.insert(i - 1, tmp)
        # i = i-1
    elif cal[i] == '-':
        tmp = cal[i-1] - cal[i+1]
        cal.remove(cal[i - 1])
        cal.remove(cal[i - 1])
        cal.remove(cal[i - 1])
        cal.insert(i - 1, tmp)
        # i = i-1
    else:
        i += 1
    if len(cal) == 1:
        break
print(cal[0])
# +-*
#
# 20 33 3 4 +-*
