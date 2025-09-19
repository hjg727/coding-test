N, M = map(int, input().split())
result = []
def bt(start, path):
    if len(path) == M:
        result.append(path[:])
        return
    
    for i in range(start, N+1):
        if i not in path:
            path.append(i)
            bt(i+1, path)
            path.pop()

bt(1, [])

for res in sorted(result):
    print(' '.join(map(str, res)))