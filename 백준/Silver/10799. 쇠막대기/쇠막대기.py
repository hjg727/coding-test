#쇠파이프

pipes = list(input())

cnt = 0
prev = ""
res = 0

for pipe in pipes:

    if pipe == "(":    
        
        cnt += 1
        prev = "("

    elif pipe == ")":

        if prev == "(":
            cnt -= 1
            res += cnt
        elif prev == ")":
            res += 1
            cnt -= 1
        prev = ")"
print(res)