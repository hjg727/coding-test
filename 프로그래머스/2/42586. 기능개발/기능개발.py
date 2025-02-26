import math
def solution(progresses, speeds):

    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    success = []
    tmp_max = days[0]
    cnt = 1
    for i in range(1, len(days)):
        if days[i] > tmp_max:
            success.append(cnt)
            tmp_max = days[i]
            cnt = 1
        else:
            cnt += 1
    
    success.append(cnt)
    return success