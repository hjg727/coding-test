
T = int(input())
ans = []
for _ in range(T):
    M, N, x, y = map(int, input().split())
    tmp = 0
    year = x
    while year <= M * N:
        if (year - 1) % N + 1 == y:
            tmp = 1
            break
        year += M
    
    ans.append(year if tmp else -1)

for i in ans:
    print(i)