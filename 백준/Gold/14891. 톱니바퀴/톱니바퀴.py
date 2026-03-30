#N극 0, S극 1
from collections import deque
tob = []
for _ in range(4):
    a = deque(map(int, input()))
    tob.append(a)

#0->12시방향 2-> 3시방향 6->9시방향


k = int(input())
#1인경우 rotate, -1인경우 rerotate
for _ in range(k):
    a, b = map(int, input().split())
    a-=1

    rotate_dir=[0]*4
    rotate_dir[a] = b

    for i in range(a-1,-1,-1):
        if tob[i][2] != tob[i+1][6]:
            rotate_dir[i] = -rotate_dir[i+1]
        else:
            break
    
    for i in range(a+1, 4):
        if tob[i][6] != tob[i-1][2]:
            rotate_dir[i] = -rotate_dir[i-1]
        else:
            break
    
    for i in range(4):
        if rotate_dir[i] != 0:
            tob[i].rotate(rotate_dir[i])

res = sum(2**i for i in range(4) if tob[i][0] == 1)
print(res)