import sys
sys.setrecursionlimit(10**6)
n = int(input())
computers = [[] for _ in range(n)]
tmp = int(input())
visited = [False] * n

for _ in range(tmp):
    a, b = map(int, input().split())
    computers[a-1].append(b-1)
    computers[b-1].append(a-1)
res = 0

def dfs(node):
    global res
    visited[node] = True

    for i in computers[node]:
        if not visited[i]:
            dfs(i)
            res += 1
dfs(0)

print(res)