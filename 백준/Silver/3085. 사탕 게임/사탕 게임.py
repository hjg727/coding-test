N = int(input())

field = []
for _ in range(N):
    field.append(list(input().rstrip()))
res = 0
def find_max_cnt(line):
    previous = line[0]
    cnt = 1
    curr = 1
    for candy in line[1:]:
        if candy == previous:
            curr += 1
            cnt = max(cnt, curr)
        else:
            previous = candy
            curr = 1
    return cnt

def change_candy(field, x1, y1, x2, y2):
    field[x1][y1], field[x2][y2] = field[x2][y2], field[x1][y1]
    max_candy = 0
    for row in set([x1, x2]):
        max_candy = max(max_candy, find_max_cnt(field[row]))
    
    for col in set([y1, y2]):
        lines = [field[row][col] for row in range(N)]
        max_candy = max(max_candy, find_max_cnt(lines))
    field[x1][y1], field[x2][y2] = field[x2][y2], field[x1][y1]

    return max_candy

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            res= max(res, change_candy(field, i, j, i, j+1))
        if i + 1 < N:
            res= max(res, change_candy(field, i, j, i+1, j))

print(res)