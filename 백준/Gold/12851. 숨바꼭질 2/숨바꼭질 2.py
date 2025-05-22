from collections import deque
n, k = map(int, input().split())
    
    # 같은 위치에 있는 경우
if n == k:
    print(0)
    print(1)
    exit(0)

# BFS를 위한 설정
max_pos = 100000
visited = [-1] * (max_pos + 1)  # 각 위치에 도달하는 최단 시간
count = [0] * (max_pos + 1)     # 각 위치에 도달하는 방법의 수

queue = deque([n])
visited[n] = 0
count[n] = 1

while queue:
    current = queue.popleft()
    
    # 목적지에 도달한 경우
    if current == k:
        print(visited[k])
        print(count[k])
        break
    
    # 가능한 세 가지 이동: -1, +1, *2
    next_positions = []
    
    # 뒤로 한 칸 이동
    if current - 1 >= 0:
        next_positions.append(current - 1)
    
    # 앞으로 한 칸 이동
    if current + 1 <= max_pos:
        next_positions.append(current + 1)
    
    # 순간이동 (2배)
    if current * 2 <= max_pos:
        next_positions.append(current * 2)
    
    for next_pos in next_positions:
        # 처음 방문하는 경우
        if visited[next_pos] == -1:
            visited[next_pos] = visited[current] + 1
            count[next_pos] = count[current]
            queue.append(next_pos)
        
        # 같은 시간에 도달하는 다른 경로가 있는 경우
        elif visited[next_pos] == visited[current] + 1:
            count[next_pos] += count[current]