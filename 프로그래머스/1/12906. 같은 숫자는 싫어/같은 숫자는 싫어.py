def solution(arr):
    tmp = None
    answer = []
    for a in arr:
        if a != tmp:
            answer.append(a)
            tmp = a
    return answer


print(solution([4,4,4,3,3]))