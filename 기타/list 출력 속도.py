import time
start = time.time()

ans = [i for i in range(10000)]
# len = 5000
# 0.006986379623413086
# len = 10000
# 0.004003047943115234
print(' '.join(map(str, ans)))

# len = 5000
# 0.07579708099365234
# len = 10000
# 0.22838973999023438
print(*ans)

print("time :", time.time() - start)
