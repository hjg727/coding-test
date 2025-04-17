E, S, M = map(int, input().split())
years=1

while True:
    if ((years-E)%15==0) and ((years-S)%28 == 0) and ((years-M)%19==0):
        print(years)
        break
    years+=1