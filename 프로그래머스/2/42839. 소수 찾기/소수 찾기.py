import itertools
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def solution(numbers):
    ans = set()
    for i in range(1, len(numbers)+1):
        for per in itertools.permutations(numbers, i):
            ans.add(int("".join(per)))
    cnt = 0
    for i in ans:
        print(i)
        if is_prime(i):
            cnt += 1
    return cnt