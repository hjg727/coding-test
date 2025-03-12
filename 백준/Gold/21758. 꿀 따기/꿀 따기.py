N = int(input())

field = list(map(int, input().split()))

ans = []

def bee_bee_bucket(field):
    max_val = -1
    tmp = [0] * N
    for i in range(1, N):
        tmp[i] = tmp[i-1] + field[i]

    for i in range(1, N):
        val = 2*tmp[N-1] - (field[i]*2) - tmp[i-1]
        max_val = max(max_val, val)
    
    return max_val

def bee_bucket_bee(field):
    max_val = -1
    tmp = [0] * N
    for i in range(1, N-1):
        tmp[i] = tmp[i-1] + field[i]

    for i in range(1, N-1):
        val = tmp[N-2] + field[i]
        max_val = max(max_val, val)
    return max_val

ans.append(bee_bee_bucket(field))
ans.append(bee_bucket_bee(field))
ans.append(bee_bee_bucket(field[::-1]))
print(max(ans))
