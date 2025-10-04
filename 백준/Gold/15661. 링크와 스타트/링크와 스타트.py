N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
res =1e9
total = 0
powers = [0]*N

for i in range(N):
    for j in range(N):
        total += S[i][j]
        powers[i] += S[i][j]
        powers[j] += S[i][j]

def bt(t, idx=0):
    global res
    res = min(res, abs(t))
    if res == 0:
        return
    for i in range(idx+1, N):
        bt(t-powers[i], i)

bt(total)
print(res)