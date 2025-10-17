def solution(n, computers):
    visited = [False] * n
    cnt = 0

    def dfs(node):
        visited[node] = True

        for n_node in range(n):
            if computers[node][n_node] == 1 and not visited[n_node]:
                dfs(n_node)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1
    return cnt
