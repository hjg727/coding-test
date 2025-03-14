def solution(edges):
    # 최대 정점 번호 계산
    N = max(max(row) for row in edges)
    
    # 나가는 간선과 들어오는 간선 수 계산
    x_count = {}  # 나가는 간선 수
    y_count = {}  # 들어오는 간선 수
    for x, y in edges:
        x_count[x] = x_count.get(x, 0) + 1  # 나가는 간선
        y_count[y] = y_count.get(y, 0) + 1  # 들어오는 간선

    # 중심 정점 찾기: 들어오는 간선이 없고, 나가는 간선이 2개 이상
    mid = None
    for i in range(1, N+1):
        if y_count.get(i, 0) == 0 and x_count.get(i, 0) >= 2:
            mid = i
            break

    # 중심 정점이 없으면 문제 조건에 맞지 않음
    if mid is None:
        return [0, 0, 0, 0]

    # 그래프 개수 계산
    eight = 0  # 8자 그래프 수
    stick = 0  # 막대 그래프 수

    for i in range(1, N+1):
        if i != mid:  # 중심 정점 제외
            if not x_count.get(i, 0) and y_count.get(i, 0) > 0:
                stick += 1  # 막대 그래프 끝점
            elif x_count.get(i, 0) >= 2 and y_count.get(i, 0) >= 2:
                eight += 1  # 8자 그래프

    # 도넛 그래프 수 계산
    donut = x_count[mid] - stick - eight

    return [mid, donut, stick, eight]