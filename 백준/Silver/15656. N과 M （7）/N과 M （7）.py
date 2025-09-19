N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))

def bt(path):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    
    for i in range(len(num)):
        path.append(num[i])
        bt(path)
        path.pop()

bt([])
