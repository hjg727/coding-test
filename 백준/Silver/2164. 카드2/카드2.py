from collections import deque

N = int(input())

q = deque([i for i in range(1, N+1)])

def operation(q):
    q.popleft()
    tmp = q.popleft()
    q.append(tmp)
    return q

while len(q) != 1:
    operation(q)

print(q.pop())