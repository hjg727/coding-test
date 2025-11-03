N = int(input())
num = list(map(int, input().split()))

dp = [1] * N
arr = [-1] * N
for i in range(1, N):
    for j in range(i):
        if num[j] < num[i]:
            if dp[i] < dp[j]+1:
                dp[i] = dp[j] + 1
                arr[i] = j

length = max(dp)
idx = dp.index(length)
res = []

while idx != -1:
    res.append(num[idx])
    idx = arr[idx]

res.reverse()

print(length)
print(*res)

