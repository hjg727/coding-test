def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)

    answer = n

    def count(start, cnt, visited):
        visited[start] = start
        cnt = 1
        for i in graph[start]:
            if visited[i] == 0:
                cnt += count(i, cnt, visited)
        return cnt
    
    for x,y in wires:
        graph[x].remove(y)
        graph[y].remove(x)

        visited = [0] * (n+1)

        a = count(x, 0, visited)
        b = n-a
        temp = abs(a-b)
        answer = min(answer, temp)
        graph[x].append(y)
        graph[y].append(x)

    return answer