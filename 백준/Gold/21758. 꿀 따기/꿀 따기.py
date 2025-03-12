N = int(input())

field = list(map(int, input().split()))

ans = []

def bee_bee_bucket(field):
    max_val = -1\
    
    for i in range(1, N-1):
        val = sum(field[1:N]) * 2 - (field[i]*2) - sum(field[1:i])
        max_val = max(max_val, val)
    
    return max_val

def bee_bucket_bee(filed):
    max_val = -1

    for i in range(1, N-1):
        val = field[i] * 2
        val += sum(field[1:i])
        val += sum(field[i+1:N-1])
        max_val = max(max_val, val)
    return max_val

ans.append(bee_bee_bucket(field))
ans.append(bee_bucket_bee(field))
ans.append(bee_bee_bucket(field[::-1]))
print(max(ans))