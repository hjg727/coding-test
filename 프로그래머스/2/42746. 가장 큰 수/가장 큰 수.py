def solution(numbers):
    numbers = list(map(str, numbers))
    answer = ''
    numbers.sort(key= lambda x : x*3, reverse=True)
    for i in numbers:
        answer += i 
    return str(int(answer))