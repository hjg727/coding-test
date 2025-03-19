def solution(word):
    sheet = ['A', 'E', 'I', 'O', 'U']
    dict_all = []

    def dfs(current, length):
        if len(current) > 5:
            return
        
        if current:
            dict_all.append(current)
        
        for word in sheet:
            dfs(current+word, length +1 )
    
    dfs("", 0)
    dict_all.sort()
    return dict_all.index(word) + 1