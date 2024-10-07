# https://school.programmers.co.kr/learn/courses/30/lessons/118668
# https://github.com/encrypted-def/kakao-blind-recruitment/blob/master/2022-summer-internship/Q3.py

def solution(alp, cop, problems):
    # 최소시간
    alp_max = max(problem[0] for problem in problems)
    cop_max = max(problem[1] for problem in problems)
    
    # alp, cop 시작값이 max보다 크면 안됨
    alp = min(alp, alp_max)
    cop = min(cop, cop_max)
    
    INF = int(1e9)
    dp = [[INF]*(cop_max+1) for _ in range(alp_max+1)]
    dp[alp][cop] = 0
    
    for i in range(alp, alp_max+1):
        for j in range(cop, cop_max+1):
            if i < alp_max:
                dp[i+1][j] = min(dp[i][j]+1, dp[i+1][j])
            if j < cop_max:
                dp[i][j+1] = min(dp[i][j]+1, dp[i][j+1])
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i < alp_req or j < cop_req:
                    continue
                alp_nx = min(alp_max, i + alp_rwd)
                cop_nx = min(cop_max, j + cop_rwd)
                dp[alp_nx][cop_nx] = min(dp[alp_nx][cop_nx], dp[i][j]+cost)
    # print(dp[alp_max][cop_max])
    
    return dp[alp_max][cop_max]