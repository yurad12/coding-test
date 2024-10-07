# https://school.programmers.co.kr/learn/courses/30/lessons/49191

'''
4 <- 3 <- 2 <- 5
1 <- 2 <- 5

winners: i를 이긴 선수들
losers: i에게 진 선수들
losers은 winners에게도 진다
'''

def solution(n, results):
    answer = 0
    indegree = [set() for _ in range(n+1)]
    outdegree = [set() for _ in range(n+1)]
    for w, l in results:
        indegree[l].add(w)
        outdegree[w].add(l)
    
    for i in range(1,n+1):
        winners = indegree[i]
        for w in winners:
            losers = outdegree[i]
            for l in losers:
                indegree[l].add(w)
                outdegree[w].add(l)
                
    for i in range(1,n+1):
        if len(indegree[i]) + len(outdegree[i]) == n-1:
            answer += 1
    return answer