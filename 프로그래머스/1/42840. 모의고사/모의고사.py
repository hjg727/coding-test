def solution(answers):
    student = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    answer = []
    score = [0, 0, 0]
    for i in range(len(student)):
        tmp = student[i]
        for j in range(len(answers)):
            if tmp[j%len(tmp)] == answers[j]: score[i] += 1


    max_value = max(score)
    if score[0] == max_value: answer.append(1)
    if score[1] == max_value: answer.append(2)
    if score[2] == max_value: answer.append(3)
    return answer