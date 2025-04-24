T = int(input())
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = sum(dp[i-3:i])

for _ in range(T):
    N = int(input())
    print(dp[N])