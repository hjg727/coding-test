N = int(input())

day = [0]
money = [0]

for _ in range(N):
    a, b = map(int, input().split())
    day.append(a)
    money.append(b)

res = -1
def bt(cnt, hap):
    global res
    if cnt > N:
        res = max(res, hap)
        return
    #안한다.
    bt(cnt+1, hap)

    #한다.
    if cnt + day[cnt] <= N+1:
        bt(cnt+day[cnt], hap+money[cnt])
bt(1, 0)
print(res)