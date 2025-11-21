#1,1에서 N,M으로 이동할때 최댓값을 구하기
N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

dp[0][0] = field[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + field[0][i]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + field[i][0]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + field[i][j]

print(dp[N-1][M-1])