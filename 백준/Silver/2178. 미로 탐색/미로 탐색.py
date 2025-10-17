N, M = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(N)]

from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]
visited = [[False] * M for _ in range(N)]

queue = deque([(0,0)])
visited[0][0] = True

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and maps[nx][ny] == 1:
            maps[nx][ny] = maps[x][y] + 1
            visited[nx][ny] = True
            queue.append((nx, ny))
print(maps[N-1][M-1])