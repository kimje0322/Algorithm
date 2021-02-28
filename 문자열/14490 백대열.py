n, m = map(int, input().split(':'))
def gcd(a,b):
    while b>0:
        tmp = a
        a = b
        b = tmp % b
    return a
a = gcd(n,m)
print('%d:%d' % (n//a, m//a))

# i = 1
# if n == m:
#     print('1:1')
# else:
#     while True:
#         i += 1
#         if not(n%i) and not(m%i):
#             n, m = n//i, m//i
#             if n == 1 or m == 1:
#                 break
#             i -= 1
#         if (n in [1,2,3,5,7]) and (m%n) or (m in [1,2,3,5,7]) and (n%m):
#             break
#         if min(n,m) < i:
#             break
#     print('%d:%d' % (n, m))