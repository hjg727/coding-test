N = int(input())

day = [0]
money = [0]

for _ in range(N):
    a, b = map(int, input().split())
    day.append(a)
    money.append(b)

dp = [0]*(N+2)

for i in range(N, 0, -1):

    if i + day[i] <= N+1:
        dp[i] = max(dp[i+1], money[i] + dp[i + day[i]])
    else:
        dp[i] = dp[i+1]
print(dp[1])