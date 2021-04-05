def selection_sort(lst):
    n = len(lst)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[min_idx], lst[i] = lst[i], lst[min_idx]
    print(lst)

selection_sort([5,7,2,4,3,1])

# def selection_sort(lst):
#     n = len(lst)
#     for i in range(n-1):
#         min_idx = i
#         for j in range(i+1, n):
#             if lst[j] < lst[min_idx]:
#                 min_idx = j
#         lst[i], lst[min_idx] = lst[min_idx], lst[i]
#     print(lst)
#
# selection_sort([0, 4, 5, 1, 3, 2])