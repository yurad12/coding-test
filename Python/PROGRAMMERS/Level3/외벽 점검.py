# https://school.programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations

def solution(n, weak, dist):
    # 원형 -> 직선
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    
    # 최소 점검 인원 체크, 점검할 수 없는 경우
    answer = len(dist)+1

    # 각 지점 시작지점으로 탐색
    for start in range(length):
        # 점검할 친구들 순서 후보들로 탐색
        for friends in list(permutations(dist,len(dist))):
            count = 1
            position = weak[start] + friends[count-1]
            # 후보 친구가 탐색할 수 있는 최대 취약 지점 확인
            # 직선으로 폈기 때문에 (현재 위치+weak개수)
            for idx in range(start,start+length):
                # position이 취약점 위치보다 작은 경우, 새로운 친구 투입
                if position < weak[idx]:
                    count += 1
                    if count > len(dist):
                        break
                    # 새로 투입된 친구가 탐색할 수 있는 최대 취약 지점 확인
                    position = weak[idx] + friends[count-1]
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1            
    return answer