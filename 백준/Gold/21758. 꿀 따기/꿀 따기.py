N = int(input())

field = list(map(int, input().split()))

ans = []

def bee_bee_bucket(field):
    max_val = -1
    visited = [False] * N
    visited[0] = True
    
    for i in range(1, N-1):
        visited[i] = True
        val = 0
        for j in range(N):
            if not visited[j]:
                if j > i:
                    val += 2*field[j]
                else:
                    val += field[j]
        
        max_val = max(max_val, val)
        visited[i] = False
    
    return max_val

def bee_bucket_bee(filed):
    max_val = -1

    for i in range(1, N-1):
        val = field[i] * 2

        for j in field[1:i]:
            val += j
        for k in field[i+1:N-1]:
            val += k
        max_val = max(max_val, val)
    return max_val

ans.append(bee_bee_bucket(field))
ans.append(bee_bucket_bee(field))
ans.append(bee_bee_bucket(field[::-1]))
print(max(ans))