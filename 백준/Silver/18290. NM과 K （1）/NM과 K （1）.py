N, M, K = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
result = float('-inf')  # 변경 1: 음수 값도 고려하여 -inf로 초기화

visited = [[False] * M for _ in range(N)]

def validate(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if visited[x][y]:
        return False
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
            return False
    
    return True


def bt(cnt, start_idx, sum_num):
    global result
    if cnt == K:
        result = max(result, sum_num)
        return

    remaining_cells = N * M - start_idx
    needed_cells = K - cnt
    if remaining_cells < needed_cells:
        return

    for idx in range(start_idx, N * M):
        i = idx // M  # 행
        j = idx % M   # 열
        
        if validate(i, j):
            visited[i][j] = True
            bt(cnt + 1, idx + 1, sum_num + field[i][j])
            visited[i][j] = False

bt(0, 0, 0)

print(result)