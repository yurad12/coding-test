# https://www.acmicpc.net/problem/20437
'''
조건1: 문자 k개 포함 짧은 문자열 길이 -> 처음 나온 문자가 k위치에 나올 때가 최소 거리
조건2: 문자 k개 포함 & 첫 번째 글자와 마지막 글자 동일한 긴 문자열 길이
조건3: 조건1, 2 둘 다 해당 안되면 -1

1. 문자 위치 저장
2. 문자 위치들에서 k만큼의 거리로 최소, 최대 거리 구하기
'''

import sys
input = sys.stdin.readline
from collections import defaultdict

def solution(w, k):
    str_dict = defaultdict(list)
    for i, word in enumerate(w):
        str_dict[word].append(i)

    result = []
    for i in str_dict.values():
        for j in range(len(i)-k+1):
            result.append(i[j+k-1] - i[j] + 1)

    if result:
        result.sort()
        print(result[0], result[-1])
    else:
        print(-1)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        w = input().strip()
        k = int(input())
        solution(w,k)
