# https://www.acmicpc.net/problem/4659

import sys

def solution(test_case):
    vowels = set(['a', 'e', 'i', 'o', 'u'])

    for case in test_case:
        flag = 0
        v, c, prev = 0, 0, ''
        for s in case:
            # 모음, 자음 체크
            if s in vowels:
                v += 1
                flag = 1
                if prev not in vowels:
                    c = 0
                if s == prev and s not in set(['e','o']):
                    flag = 0
                    break
                prev = s
            else:
                c += 1
                if prev in vowels:
                    v = 0
                if s == prev:
                    flag = 0
                    break
                prev = s

            # 모음 3개 or 자음 3개 연속 체크
            if v == 3 or c == 3:
                flag = 0
                break
        if not flag:
            print("<%s> is not acceptable."%case)
        else:
            print("<%s> is acceptable."%case)    

if __name__ == "__main__":
    input = sys.stdin.readline
    test_case = []
    while True:
        case = input().strip()
        if case == "end":
            break
        test_case.append(case)
    solution(test_case)