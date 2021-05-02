from queue import PriorityQueue
que = PriorityQueue()
que.put(4)
que.put(7)
print(que)
# 이거 왜 에러?
# line 1, in <module>
#     from queue import PriorityQueue
# ImportError: cannot import name 'PriorityQueue' from 'queue'