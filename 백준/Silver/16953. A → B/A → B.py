A, B = map(int, input().split())
cnt = 0

while A < B:
    if B % 2 == 0:
        B //= 2
        cnt += 1
    elif B % 10 == 1:
        B //= 10
        cnt += 1
    else:
        break

if B == A:
    print(cnt + 1)
else:
    print(-1)