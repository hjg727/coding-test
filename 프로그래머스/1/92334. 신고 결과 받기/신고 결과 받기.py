from collections import defaultdict

def solution(id_list, report, k):

    report = set(report)
    reported_by = defaultdict(set)
    mail_cnt = {name: 0 for name in id_list}

    for r in report:
        user, target = r.split()
        reported_by[target].add(user)

    for target, reporters in reported_by.items():
        if len(reporters) >= k:
            for user in reporters:
                mail_cnt[user] += 1
    return [mail_cnt[id] for id in id_list]