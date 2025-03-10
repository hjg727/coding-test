from collections import deque

def check(x, y, field, N, M):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or N<=nx or ny<0 or M<=ny or field[nx][ny] == 0:#이건 외부에서 접근한 경우
            return True
    return False

def check2(x, y, field, N, M):
    queue = deque([])
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        dx = [1,-1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append((nx,ny))



def solution(storage, requests):
    N = len(storage)
    M = len(storage[0])
    field = []
    for i in range(len(storage)):
        field.append(list(storage[i]))
    for i in requests:
        if len(i) == 1:
            storage_remove(i,field, N, M)
        else:
            storage_all(i,field, N, M)
        for i in range(N):
            for j in range(M):
                if field[i][j] == 0:
                    check2(i, j, field, N, M)
        

    cnt = 0
    for row in field:
        for item in row:
            if isinstance(item, str):
                cnt += 1

    return cnt

def storage_remove(command, field, N, M):#지게차
    ans = []
    
    for i in range(N):
        for j in range(M):
            if field[i][j] == command and check(i, j, field, N, M):
                ans.append((i,j))

    for x, y in ans:
        field[x][y] = 0
        

    
        
    
def storage_all(command, field, N, M):#크레인
    for i in range(N):
        for j in range(M):
            if field[i][j] == command[0]:
                if check(i,j,field,N,M): # 크레인 기준에서 주변이 외부유입가능?
                    field[i][j] = 0
                else:
                    field[i][j] = 1
