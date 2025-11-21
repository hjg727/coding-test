N = int(input())
A = list(map(int, input().split()))

dp = [1001]*N
dp[0] = 0
for i in range(1, N):
    for j in range(i):
        if A[j] >= (i-j):
            dp[i] = min(dp[i], dp[j]+1)

print(dp[N-1] if dp[N-1] != 1001 else -1)