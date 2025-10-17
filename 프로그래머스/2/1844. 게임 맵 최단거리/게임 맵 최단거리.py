from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    queue = deque([(0,0)])
    visited[0][0] = True

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] and not visited[nx][ny]:
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return maps[n-1][m-1] if visited[n-1][m-1] else -1