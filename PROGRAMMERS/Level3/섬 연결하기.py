'''
https://school.programmers.co.kr/learn/courses/30/lessons/42861

최소 비용, 사이클 고려 -> 크루스칼
1. 건설 비용 오름차순 정렬
2. 사이클 체크, 다리 개수+1, answer+거리
3. 유니온 파인드 -> 사이클 생기지 않는 간선 추가
'''

def solution(n, costs):
    answer = 0
    bridge = 0
    cycle = {i:i for i in range(n)}
    costs.sort(key = lambda x: x[2])
    
    for a, b, cost in costs:
        if a > b:
            a, b = b, a
        if cycle[a] == cycle[b]:
            continue
        answer += cost
        bridge += 1
        
        prev = cycle[b]
        cycle[b] = cycle[a]
        for i, v in cycle.items():
            if v == prev:
                cycle[i] = cycle[a]

        if bridge == n-1:
            break
    return answer