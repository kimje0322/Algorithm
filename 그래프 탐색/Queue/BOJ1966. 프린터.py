case = int(input())

for _ in range(case):
    N, M = map(int, input().split())
    print_list = list(map(int, input().split()))
    prior_number = []

    for doc in print_list:
        prior_number.append(doc)

    result = [0 for _ in range(N)]
    queue = [i for i in range(N)]
    sequence = 1
    while queue:
        if print_list[queue[0]] == max(prior_number):
            prior_number.remove(max(prior_number))
            result[queue.pop(0)] = sequence
            sequence += 1
        else:
            queue.append(queue.pop(0))
    print(result[M])