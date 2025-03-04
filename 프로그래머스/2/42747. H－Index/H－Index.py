def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)
    answer = 0
    for i in range(n):
        if citations[i] > i:
            answer = i+1
        else:
            break
    
    return answer