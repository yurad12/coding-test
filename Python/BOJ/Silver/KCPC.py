# https://www.acmicpc.net/problem/3758
'''
팀의 개수 n, 문제의 개수 k, 당신 팀의 ID t, 로그 엔트리의 개수 m
팀 ID i, 문제 번호 j, 획득한 점수 s
'''

import sys
input = sys.stdin.readline

def solution(n, k, t, m, submits: list, count:list, time:list):
    scores = []
    for i in range(n):
        scores.append([sum(submits[i]), count[i], time[i], i]) # i: 팀 번호
    scores.sort(key = lambda x: (-x[0], x[1], x[2])) # 최종 점수 -> 횟수 -> 시간

    for i in range(n):
        if scores[i][3] == t-1:
            print(i+1)
    return i+1

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, k, t, m = map(int, input().split())
        submits = [[0] * k for _ in range(n)] # 팀 + 문제번호
        count = [0] * n
        time = [0] * n

        for idx in range(m):
            id, j, s = map(int, input().split())
            submits[id-1][j-1] = max(submits[id-1][j-1], s)
            time[id-1] = idx
            count[id-1] += 1
        solution(n, k, t, m, submits, count, time)
