def solution(prices):
    len_p = len(prices)
    answer = []
    for i in range(len_p):
        if i == len_p-1:
            answer.append(0)
        for j in range(i+1, len_p):
            if prices[i] > prices[j] or j+1==len_p:
                answer.append(j-i)
                break
            

    return answer
