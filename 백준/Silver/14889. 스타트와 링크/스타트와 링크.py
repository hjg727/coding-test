N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

res = 1e9
total = 0
powers = [0] * N
for i in range(N):
    for j in range(N):
        total += S[i][j]
        powers[i] += S[i][j]
        powers[j] += S[i][j]

def bt(path, start):
    global res
    global total
    if len(path) == N//2:
        a=0
        for i in path:
            a += powers[i]
        res = min(res, abs(total-a))
        return
    if res == 0:
        return
    for i in range(start, N):
        if i not in path:
            path.append(i)
            bt(path, i+1)
            path.pop()
bt([], 0)
print(res)
