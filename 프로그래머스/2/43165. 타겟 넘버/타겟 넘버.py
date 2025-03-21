import sys
sys.setrecursionlimit(10**6)

def solution(numbers, target):
    def dfs(numbers, target, index, current):
        if len(numbers) == index:
            if target == current:
                return 1
            else:
                return 0
        
        return dfs(numbers, target, index+1, current+numbers[index]) + dfs(numbers, target, index+1, current-numbers[index])
    return dfs(numbers, target, 0, 0)