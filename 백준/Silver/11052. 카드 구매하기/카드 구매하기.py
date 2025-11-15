N = int(input())  # 구매하려는 카드 개수 입력 받기
prices = [0] + list(map(int, input().split()))  # 가격 정보 입력 받기

dp = [0] * (N+1)  # 최소 비용 저장 배열 초기화

for i in range(1, N+1):
    dp[i] = max(prices[j] + dp[i-j] for j in range(1, i+1))

print(dp[N])  # N개의 카드를 구매하는 최소 비용 출력
