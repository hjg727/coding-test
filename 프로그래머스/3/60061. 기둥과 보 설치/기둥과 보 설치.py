def can_install(col, beam, x, y, a):
    if a == 0:  # 기둥 설치 조건
        # 바닥 위, 보의 한쪽 끝 부분 위, 또 다른 기둥 위
        return y == 0 or [x, y-1, 0] in col or [x-1, y, 1] in beam or [x, y, 1] in beam
    else:  # 보 설치 조건
        # 한쪽 끝 부분이 기둥 위, 양쪽 끝 부분이 다른 보와 동시에 연결
        return ([x, y-1, 0] in col or [x+1, y-1, 0] in col) or ([x-1, y, 1] in beam and [x+1, y, 1] in beam)

def can_delete(cols, beams):
    # 모든 기둥과 보가 아직 유효한지 확인
    for x, y, a in cols + beams:
        if not can_install(cols, beams, x, y, a):
            return False
    return True

def solution(n, build_frame):
    cols = []
    beams = []
    
    for x, y, a, b in build_frame:
        element = [x, y, a]
        if b == 0:  # 삭제하는 경우
            if a == 0:
                cols.remove(element)
            else:
                beams.remove(element)
            if not can_delete(cols, beams):
                if a == 0:
                    cols.append(element)
                else:
                    beams.append(element)
        else:  # 설치하는 경우
            if can_install(cols, beams, x, y, a):
                if a == 0:
                    cols.append(element)
                else:
                    beams.append(element)
    
    result = cols + beams
    result.sort()
    return result