from collections import deque

def solution(n, computers):
    visited = [False] * n
    queue = deque()
    answer = 0
    for i in range(n):
        
        if visited[i] == False:
            queue.append(i)

            while queue:
                x = queue.popleft()
                visited[x] = True

                for j in range(n):
                    if not visited[j] and computers[x][j] == 1:
                        queue.append(j)

            answer += 1
    return answer
        