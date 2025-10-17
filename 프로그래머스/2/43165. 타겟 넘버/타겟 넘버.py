from collections import deque
def solution(numbers, target):
    def bfs(numbers, target):
        queue = deque([(0,0)])
        cnt = 0

        while queue:
            idx, current = queue.popleft()

            if idx == len(numbers):
                if current == target:
                    cnt += 1

            else:
                queue.append((idx+1, current+numbers[idx]))
                queue.append((idx+1, current-numbers[idx]))
        return cnt
    return bfs(numbers, target)