S = input()
S_slice = []
start = 0
count_0 = 0
count_1 = 0

for i in range(len(S) + 1):
    if int(i) == len(S) - 1:
        S_slice.append(S[start:])
        if S[start] == '0':
            count_0 += 1
        else:
            count_1 += 1
        break

    if S[i] != S[i + 1]:
        S_slice.append(S[start:i + 1])
        if S[start] == '0':
            count_0 += 1
        else:
            count_1 += 1

        start = i + 1

print(min(count_0, count_1))