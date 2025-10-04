from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

res = 10**9

#1개를 조합하고싶고 2개를 조합하고싶고 N-1개까지 조합하면 그만큼 스타트 팀은 N-1 -> 1개 어떻게 해야될까
for target in range(1, N//2 + 1):

    for team_link in combinations(range(N), target):
        
        team_link_set = set(team_link)
        team_start = [x for x in range(N) if x not in team_link_set]
        a = 0

        for i in range(len(team_link)):
            for j in range(i+1, len(team_link)):
                pi, pj = team_link[i], team_link[j]
                a += S[pi][pj] + S[pj][pi]
        
        len_team_start = N - target
        b = 0

        for i in range(len_team_start):
            for j in range(i+1, len_team_start):
                pi, pj = team_start[i], team_start[j]
                b += S[pi][pj] + S[pj][pi]
        
        res = min(res, abs(a-b))
        
        if res == 0:
            break

    if res == 0:
        break

print(res)