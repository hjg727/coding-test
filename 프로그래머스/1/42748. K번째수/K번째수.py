def solution(array, commands):
    answer = []    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])

    return answer