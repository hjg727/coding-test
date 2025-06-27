import math

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    years = 1
    tmp = 0

    max_year = math.lcm(M, N)
    answer = x
    while answer <= max_year:
        if (answer - 1) % N + 1 == y:
            break
        answer += M
    if answer > max_year:
        print(-1)
    else:
        print(answer)