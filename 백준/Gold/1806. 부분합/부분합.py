N, S = map(int, input().split())
num = list(map(int, input().split()))
hap = [0] * (N + 1)  # hap[0] = 0으로 시작, 길이 N+1로 변경
for i in range(N):
    hap[i + 1] = hap[i] + num[i]  # hap[i+1]은 0부터 i까지의 합

if hap[N] < S:  # 전체 합이 S보다 작으면 불가능
    print(0)
    exit(0)

ans = N + 1
for i in range(N):
    if num[i] >= S:  # 단일 원소가 S 이상이면
        print(1)
        exit(0)
    
    if hap[i + 1] >= S:  # i까지의 합이 S 이상이면
        left, right = 0, i
        while left <= right:
            mid = (left + right) // 2
            if hap[i + 1] - hap[mid] >= S:  # mid부터 i까지의 합
                ans = min(ans, i - mid + 1)  # 길이는 i-mid+1
                left = mid + 1
            else:
                right = mid - 1

print(ans if ans != N + 1 else 0)
