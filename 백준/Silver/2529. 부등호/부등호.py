from itertools import permutations

num = [i for i in range(10)]
k = int(input())
sign = list(input().split())
res = []
def bt(idx, path):
    if idx == k+1:
        res.append("".join(map(str, path)))
        return

    for i in range(10):
        if i in path: continue
        if idx > 0:
            if sign[idx-1] == '<' and path[-1] >= i: continue
            if sign[idx-1] == '>' and path[-1] <= i: continue
        
        result = bt(idx+1, path + [i])
        if result: return result

bt(0, [])
print(res[-1])
print(res[0])
