from collections import defaultdict
import math

def solution(fees, records):
    
    in_time = {}
    total_time = defaultdict(int)
    for record in records:
        time, car, state = record.split()
        h, m = map(int, time.split(':'))
        minutes = h*60+m

        if state == "IN":
            in_time[car] = minutes
        else:
            total_time[car] += minutes - in_time[car]
            del in_time[car]

    
    for car, time in in_time.items():
        total_time[car] += (23*60+59) - time

    basic_time, basic_fee, unit_time, unit_fee = fees

    answer = []
    for car in sorted(total_time.keys()):
        time = total_time[car]

        if time<=basic_time:
            fee = basic_fee
        else:
            fee = basic_fee + math.ceil((time-basic_time)/unit_time)*unit_fee
        answer.append(fee)
    return answer
