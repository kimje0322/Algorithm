# hash 풀이
def solution(participant, completion):
    answer = ''
    tmp = 0
    dic = {}

    for part in participant:
        dic[hash(part)] = part
        tmp += hash(part)
    for com in completion:
        tmp -= hash(com)
    return (dic[tmp])
