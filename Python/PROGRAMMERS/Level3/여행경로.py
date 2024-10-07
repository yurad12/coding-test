'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/43164

1. 티켓 딕셔너리 만들기: key(출발), item(도착)
2. 티켓 딕셔너리 item 내림차순 정렬
3. 티켓 탐색하면서 공항들 스택에 넣기
 - 티켓 딕셔너리의 item에서 공항 pop
 - 스택의 마지막에 들어온 공항에서 더 갈 공항이 있는지 확인
 - 더이상 방문할 공항이 없으면 path에 추가
4. 마지막으로 방문할 공항순으로 path에 추가했기 때문에 path.reverse()
5. return path

주의할 부분
[["ICN", "A"], ["ICN", "B"], ["B", "ICN"]] -> ["ICN", "B", "ICN", "A"]
'''

def solution(tickets):
    tickets_dict = {}
    for depart, arrival in tickets:
        if depart not in tickets_dict:
            tickets_dict[depart] = []
        tickets_dict[depart].append(arrival)
    
    for key in tickets_dict.keys():
        tickets_dict[key].sort(reverse=True)

    stack = ['ICN'] # LIFO
    path = []
    while len(stack) > 0:
        now = stack[-1]
        if now not in tickets_dict or not tickets_dict[now]:
            path.append(stack.pop())
            continue
        stack.append(tickets_dict[now].pop())
    
    path.reverse()
    return path
