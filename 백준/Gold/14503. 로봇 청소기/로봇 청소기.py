dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def left(d):
    return (d+3)%4

# 50*50-> 2500

n, m = map(int, input().split())
y, x, d = map(int, input().split())

field = []
for _ in range(n):
    field.append(list(map(int , input().split())))
field[y][x] = 2
cnt = 1
while True:
    clean = False

    for _ in range(4):
        d = left(d)
        ny = y + dy[d]
        nx = x + dx[d]
        
        if field[ny][nx] == 0:
            field[ny][nx] = 2
            cnt += 1
            y, x= ny, nx
            clean = True
            break

    if not clean:
        if field[y - dy[d]][x-dx[d]] == 1:
            break
        else:
            y -= dy[d]
            x -= dx[d]
print(cnt)