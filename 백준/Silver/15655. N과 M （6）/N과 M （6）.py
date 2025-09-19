N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
res = []
def bt(start, path):
    if len(path) == M:
        res.append(path[:])
        return
    
    for i in range(start, len(num)):
        # if i not in path:
        path.append(num[i])
        bt(i+1, path)
        path.pop()

bt(0, [])

for num in sorted(res):
    print(' '.join(map(str, num)))