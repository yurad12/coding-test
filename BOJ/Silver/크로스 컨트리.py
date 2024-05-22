# https://www.acmicpc.net/problem/9017

import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    race = list(map(int, input().split()))
    
    # 팀 수 찾기
    team_numbers = defaultdict(int)
    for team in race:
        team_numbers[team] += 1
    
    # 팀 점수 계산하기
    team_scores = defaultdict(list)
    count = 1
    for team in race:
        if team_numbers[team] != 6:
            continue
        team_scores[team].append(count)
        count += 1

    # 우승 팀 계산하기
    result, winner = int(1e9), -1
    for team in team_scores.keys():
        sum_scores = sum(team_scores[team][:4])
        if result > sum_scores:
            result, winner = sum_scores, team
        elif result == sum_scores:
            if team_scores[winner][-2] > team_scores[team][-2]:
                result, winner = sum_scores, team

    print(winner)