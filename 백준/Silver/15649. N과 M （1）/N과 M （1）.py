import itertools

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
permutation = itertools.permutations(arr, M)

for per in permutation:
    print(*per)