import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
indexed = []
result = [-1]*N # 기본 -1 오큰수 값 못 찾으면 업데이트 안한다고 설계

for i in range(N):
    while indexed and A[indexed[-1]] < A[i]:
        index = indexed.pop()
        result[index] = A[i]
    
    indexed.append(i)

for i in range(len(result)):
    print(result[i], end=" ")