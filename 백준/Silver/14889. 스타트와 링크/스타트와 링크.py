N = int(input())
ans = 10000000000
S = [list(map(int, input().split())) for _ in range(N)]
check = [False for _ in range(N)]

def calc(start, link):
    for i in range(N):
        for j in range(N):
            if check[i] and check[j]:
                start += S[i][j]
            if not check [i] and not check[j]:
                link += S[i][j]
    return abs(start - link)
def DFS(count, cand):
    global ans
    if count == N//2:
        temp = calc(0, 0)
        if ans > temp:
            ans = temp
        return
    else:
        for i in range(cand, N):
            check[i] = True
            DFS(count + 1, i + 1)
            check[i] = False

DFS(0, 1)
print(ans)
