N = int(input())
tmp = list(input().rstrip())
matrix = []

for i in range(N, 0, -1):
    matrix.append(tmp[:i])
    tmp = tmp[i:]

def check(path, num):
    target = path + [num]
    new_idx = len(target) - 1

    cumsum = 0
    for start in range(new_idx, -1, -1):
        cumsum += target[start]
        expected = matrix[start][new_idx - start]
        
        if expected == '+' and cumsum <= 0:
            return False
        elif expected == '-' and cumsum >= 0:
            return False
        elif expected == '0' and cumsum != 0:
            return False
    
    return True

def bt(path):
    if len(path) == N:
        return path[:]
    
    for num in range(-10, 11):
        if check(path, num):
            result = bt(path + [num])
            if result:
                return result
    
    return None

res = bt([])
print(' '.join(map(str, res)))