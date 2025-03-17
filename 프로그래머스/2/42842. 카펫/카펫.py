def solution(brown, yellow):
    if yellow == 1:
        return [3,3]
    elif yellow == 2:
        return [4, 3]
    elif (yellow + 2) * 2 + 2 == brown:
        return [(yellow + 2), 3]
    else: 
        i = 2
        while i <= yellow//i:
            if yellow%i == 0:
                if (yellow//i + 2) * 2 + (2*i) == brown:
                    return [(yellow//i + 2), i+2]

            i += 1