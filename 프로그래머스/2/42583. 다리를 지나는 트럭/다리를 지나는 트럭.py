from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    current_weight = 0
    while len(truck_weights) > 0:
        time += 1
        current_weight -= bridge.popleft()
        if current_weight + truck_weights[0] > weight:
            bridge.append(0)
        else:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
    return time + bridge_length