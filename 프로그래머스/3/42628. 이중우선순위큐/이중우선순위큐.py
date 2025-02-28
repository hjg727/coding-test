import heapq

def max_out(original):
    heap = [-x for x in original]
    heapq.heapify(heap)
    return - heapq.heappop(heap)

def min_out(original):
    heap = original[:]
    heapq.heapify(heap)
    return heapq.heappop(heap)

def solution(operations):
    commands = []
    for i in operations:
        command = i[0]
        val = int(i[2:])
        commands.append((command, val))
    original = []
    while commands:
        command, val = commands.pop(0)

        if command == 'I':
            original.append(val)
        elif command == 'D' and val == -1:
            if not original:
                continue
            original.remove(min_out(original))
        else:
            if not original:
                continue
            original.remove(max_out(original))

    if original:
        min_val = min(original)
        max_val = max(original)
        return [max_val, min_val]
        
    else:
        return [0,0]
