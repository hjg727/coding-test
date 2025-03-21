from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    
    queue = deque([(0,0)])
    visited = [[False] * m for _ in range(n)]

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))

    return maps[n-1][m-1] if visited[n-1][m-1] else -1