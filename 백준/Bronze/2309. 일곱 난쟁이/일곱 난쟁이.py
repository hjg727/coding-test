nan = [int(input()) for _ in range(9)]

total = sum(nan)
found = False

for i in range(9):
    if found:
        break
    for j in range(i+1, 9):
        if total - nan[i] - nan[j] == 100:
            liar_1 = nan[i]
            liar_2 = nan[j]
            found = True
            break

nan.remove(liar_1)
nan.remove(liar_2)
nan.sort()

for nan in nan:
    print(nan)
