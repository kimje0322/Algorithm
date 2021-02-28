def enqueue(n):
    global rear
    if rear == len(queue)-1:
        print('full')
    else:
        rear += 1
        queue[rear] = n

queue = [0]*3
front = rear = -1
