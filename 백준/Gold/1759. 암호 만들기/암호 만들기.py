L, C = map(int, input().split())
chr_lst = list(map(str, input().split()))
chr_lst.sort()
vowels = ['a', 'e', 'i', 'o', 'u']

def recursion(path, start_idx):
    if len(path) == L:
        vowel_cnt = 0
        consonant_cnt = 0
        for char in path:
            if char in vowels:
                vowel_cnt += 1
            else:
                consonant_cnt += 1
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(''.join(path))  # 바로 출력
        return
    
    for i in range(start_idx, C):
        path.append(chr_lst[i])
        recursion(path, i+1)
        path.pop()

recursion([], 0)
