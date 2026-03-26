from collections import deque
N = int(input())
k = int(input())
sn = deque([(0,0)])
field = [[0]*N for _ in range(N)]
for _ in range(k):
    y, x = map(int, input().split())
    field[y-1][x-1] = 2

L = int(input()) 
cmd = deque([])

for _ in range(L):
    X, C = input().split()
    cmd.append((int(X), C))

def left(d):
    return (d+3)%4
def right(d):
    return (d+1)%4
d = 0
t = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

sn_set = {(0,0)}
while True:
    ny = sn[0][0]+dy[d]
    nx = sn[0][1]+dx[d]
        
    t+=1

    if ny < 0 or N <=ny or nx < 0 or N<=nx:
        break
    if (ny, nx) in sn_set:
        break
    
    if field[ny][nx] == 2:
        sn.appendleft((ny,nx))
        sn_set.add((ny,nx))
        field[ny][nx] = 0
    else:
        sn.appendleft((ny,nx))
        sn_set.add((ny,nx))
        tail = sn.pop()
        sn_set.remove(tail)


    if cmd and cmd[0][0] == t:
        if cmd[0][1] == 'L':
            d = left(d)
        else:
            d = right(d)
        cmd.popleft()

print(t)