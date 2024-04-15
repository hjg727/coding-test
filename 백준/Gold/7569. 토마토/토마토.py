from collections import deque

def bfs(tomatoes, m, n, h):
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    queue = deque()
    days = -1
    
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomatoes[z][y][x] == 1:
                    queue.append((x, y, z))
    while queue:
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            for dx, dy, dz in directions:
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and tomatoes[nz][ny][nx] == 0:
                    tomatoes[nz][ny][nx] = 1
                    queue.append((nx, ny, nz))
        days += 1
    
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomatoes[z][y][x] == 0:
                    return -1
    
    return days

m, n, h = map(int, input().split())
tomatoes = []
for _ in range(h):
    layer = [list(map(int, input().split())) for _ in range(n)]
    tomatoes.append(layer)

already_ripe = all(all(all(tomato == 1 for tomato in row) for row in layer) for layer in tomatoes)

if already_ripe:
    print(0)
else:
    result = bfs(tomatoes, m, n, h)
    print(result)