n = int(input())
price = [0]
price += list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = min(price[j] + dp[i-j] for j in range(1, i+1))
print(dp[n])