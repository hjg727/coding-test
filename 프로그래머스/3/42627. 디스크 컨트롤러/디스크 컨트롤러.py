import heapq
def solution(jobs):
    turn_around = 0
    ready = []
    now = 0
    cnt = 0
    jobs.sort()
    check = [False] * (len(jobs))

    while cnt < len(jobs):

        for i in range(len(jobs)):
            if jobs[i][0] <= now and not check[i]:
                heapq.heappush(ready, (jobs[i][1], jobs[i][0]))
                check[i] = True
        
        if ready:
            work, request = heapq.heappop(ready)
            now += work
            turn_around += now-request
            cnt += 1
        else:
            now += 1

    return turn_around//len(jobs)