# 바닥면과 상단은 반대되는 면인것같다.
# 이동한칸에 쓰여있는 수가 0이면 바닥-> 도장처럼 주사위 바닥의 수가 칸에 붙여넣어진다.
# 0이아니면 칸에 쓰여져있는수가 주사위 바닥에 붙여진다. 이후 칸의 정수는 0이 된다.
# 위 아래 앞 뒤 오른 왼
dice = [0, 0, 0, 0, 0, 0]
def move(x):
    if x == 1:
        # 0<-5, 1<-4, 4<-0. 5<-1
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
    elif x == 2:
        dice[5], dice[4], dice[0], dice[1] = dice[0], dice[1], dice[4], dice[5]
    elif x == 3:
        # 0<-2, 1<-3, 2<-1, 3<-0
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    elif x == 4:
        dice[2], dice[3], dice[1], dice[0] = dice[0], dice[1], dice[2], dice[3]

n, m, x, y, k = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

cmd = list(map(int, input().split()))
# 동, 서, 북, 남
dis = [(0,1),(0,-1),(-1,0), (1, 0)]
for i in range(k):
    dx, dy = dis[cmd[i]-1]
    nx = x+dx
    ny = y+dy
    if nx < 0 or n <= nx or ny < 0 or m <= ny:
        continue

    move(cmd[i])
    x, y = nx, ny
    if field[x][y] > 0:
        dice[1] = field[x][y]
        field[x][y] = 0
    else:
        field[x][y] = dice[1]
    
    print(dice[0])