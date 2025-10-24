def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def solution(numbers, hand):

    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    l_pos = (3,0)
    r_pos = (3,2)

    
    answer = ''

    for number in numbers:
        if number in (1,4,7,'*'):
            answer += 'L'
            l_pos = keypad[number]
        elif number in (3,6,9, '#'):
            answer += 'R'
            r_pos = keypad[number]
        else:
            x, y = keypad[number]
            l_dist = dist(x, y, l_pos[0], l_pos[1])
            r_dist = dist(x, y, r_pos[0], r_pos[1])

            if l_dist < r_dist:
                answer += 'L'
                l_pos = (x,y)
            elif l_dist > r_dist:
                answer += 'R'
                r_pos = (x,y)
            else:
                if hand == "right":
                    answer += 'R'
                    r_pos = keypad[number]
                elif hand == 'left':
                    answer += 'L'
                    l_pos = keypad[number]
    return answer