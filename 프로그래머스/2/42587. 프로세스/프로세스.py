from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    cnt = 0

    while priorities:
        best = max(priorities)

        front = priorities.popleft()
        location -= 1

        if front == best:
            cnt += 1
            if location < 0:
                return cnt
        else:
            priorities.append(front)
            if location < 0:
                location = len(priorities) - 1