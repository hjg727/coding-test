from itertools import permutations

num = [i for i in range(10)]
k = int(input())
sign = list(input().split())

res = []
# def bt(path, idx=0):
#     global res
#     if len(path) == k:
#         res.append(path[:])
#         return
    

#     for i in num:
#         if i not in path:
#             path.append(i)
#             bt(path)
#             path.pop()

# bt([])

for lst in permutations(num, k+1):
    check = False
    for i in range(k):
        if sign[i] == '<':
            if lst[i] < lst[i+1]:
                check = True
            else:
                check = False
                break
        else:
            if lst[i] > lst[i+1]:
                check = True
            else:
                check = False
                break
    if check:
        res.append("".join(map(str, lst)))

res.sort()
print(res[-1])
print(res[0])