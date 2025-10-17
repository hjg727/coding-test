from collections import defaultdict

def solution(id_list, report, k):
    lst = defaultdict(list)
    ids = {name: 0 for name in id_list}
    
    for report in report:
        user, target = report.split()
        if user not in lst[target]:
            lst[target].append(user)
        
    for target in lst.keys():
        if len(lst[target]) >= k:
            for user in lst[target]:
                ids[user] += 1
    answer = []
    for id in ids:
        answer.append(ids[id])
    return answer
    
    