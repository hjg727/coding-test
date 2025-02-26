import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while len(scoville) >= 2:
        min_value = heapq.heappop(scoville)

        if min_value >= K:
            return cnt
        else:
            min_value_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_value+(min_value_2*2))
            cnt += 1
    
    return cnt if scoville[0] >= K else -1