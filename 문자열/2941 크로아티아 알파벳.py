a = input()
alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# 문자열이 주어지면
# 일반 알파벳인지 변경된 알파벳인지 구분해서
# 한 글자씩 끊으면 구분이 안 되는데 어떻게 끊어내지?
#  => 문자열에서 사용할 수 있는 replace로 간단하게 해결
# 세야한다.

for i in alphabet:
    a = a.replace(i, '*')
print(len(a))