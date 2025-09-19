N, M = map(int, input().split())
num = list(map(int, input().split()))
res = []
def bt(path):
    if len(path) == M:
        res.append(path[:])
        return
    
    for i in num:
        if i not in path:
            path.append(i)
            bt(path)
            path.pop()

bt([])

for num in sorted(res):
    print(' '.join(map(str, num)))