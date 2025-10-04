N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
from itertools import combinations
res = 1e9
total = 0
powers = [0] * N
for i in range(N):
    for j in range(N):
        total += S[i][j]
        powers[i] += S[i][j]
        powers[j] += S[i][j]

for team in combinations(range(N), N//2):
    a = sum(powers[i] for i in team)
    res = min(res, abs(total-a))
    if res == 0:
        break
print(res)
