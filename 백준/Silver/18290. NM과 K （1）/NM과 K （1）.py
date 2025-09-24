N, M, K = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
result = float('-inf')

visited = [[False] * M for _ in range(N)]

def validate(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if visited[x][y]:
        return False
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
            return False
    
    return True


def bt(cnt, start_x, start_y, sum_num):
    global result
    if cnt == K:
        result = max(result, sum_num)
        return
    
    for i in range(start_x, N):
        start_j = start_y if start_x == i else 0
        for j in range(start_j, M):
            if validate(i, j):
                visited[i][j] = True
                bt(cnt+1, i, j, sum_num + field[i][j])
                visited[i][j] = False

bt(0, 0, 0, 0)

print(result)