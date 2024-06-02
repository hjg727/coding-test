from collections import deque

def turn_left(d):
    return (d+3) % 4

def turn_right(d):
    return (d+1) % 4


N = int(input())#N*N크기 map

field = [[0]*(N+1) for _ in range(N+1)]

K = int(input())

for _ in range(K):
    a, b = map(int, input().split())
    field[a][b] = 2#사과 위치 업데이트

L = int(input())

command = []

for _ in range(L):#command
    X, C = input().split()
    command.append((int(X), C))

snake=deque([(1,1)])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

time = 0
direct = 1

while True:
    x, y = snake[0]
    nx = x + dx[direct]
    ny = y + dy[direct]

    if 0<nx<=N and 0<ny<=N and not (nx, ny) in snake:
        if field[nx][ny] == 2:
            snake.appendleft((nx,ny))
            field[nx][ny] = 0
        else:
            snake.appendleft((nx,ny))
            snake.pop()
    else:
        break
    
    time += 1

    if command and time == command[0][0]:
        command_time, direction = command.pop(0)
        if direction == 'L':
            direct = turn_left(direct)
        else:
            direct = turn_right(direct)

print(time+1)