N = int(input())
day = [0] * (N+1)
money = [0] * (N+1)

for i in range(N):
    day[i], money[i] = map(int, input().split())

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if day[i] + i > N: #상담이 퇴사 날짜 넘어가면 상담을 할 수 없다
        dp[i] = dp[i+1]#맨끝날값그앞에다가 업데이트
    else:
        dp[i] = max(money[i] + dp[i+day[i]], dp[i+1])#상담on,상담x

print(dp[0])