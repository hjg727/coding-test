N, M = map(int, input().split())

def bt(path):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    
    for i in range(1, N+1):
        path.append(i)
        bt(path)
        path.pop()

bt([])