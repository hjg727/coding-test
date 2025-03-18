import itertools
def solution(k, dungeons):
    answer = -1
    for i in itertools.permutations(dungeons):
        tmp = 0
        current = k
        for x, y in i:
            if current >= x:
                current -= y
                tmp += 1

        answer = max(answer, tmp)
    
    return answer