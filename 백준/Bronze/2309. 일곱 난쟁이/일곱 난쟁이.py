small = [int(input()) for _ in range(9)]

total = sum(small)

for i in range(9):
    for j in range(i+1, 9):
        if total - small[i] - small[j] == 100:
            tall_1 = small[i]
            tall_2 = small[j]
            break
    
small.remove(tall_1)
small.remove(tall_2)

small.sort()

for small in small:
    print(small)