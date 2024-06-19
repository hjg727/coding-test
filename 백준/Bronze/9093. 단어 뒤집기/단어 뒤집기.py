import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    st = input().split()
    print(" ".join(st[::-1])[::-1])