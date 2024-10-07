# https://www.acmicpc.net/problem/1244

'''
1. 남학생: 배수 스위치 변경
2. 여학생: 좌우 대칭 +n 스위치 같을 때 스위치 변경, 다르면 현재 스위치만 변경
'''

import sys

def solution(n, statuses, m, students):
    def switch(status):
        if status:
            status = 0
        else:
            status = 1
        return status

    for i in range(m):
        sex, num = students[i]

        # 남학생
        if sex == 1:
            idx = 1
            while num*idx < n+1:
                statuses[num*idx] = switch(statuses[num*idx])
                idx += 1
        # 여학생
        elif sex == 2:
            # 해당 스위치
            statuses[num] = switch(statuses[num])
            # 주변 스위치
            idx = 1
            while True:
                if num-idx < 1 or num+idx > n:
                    break
                left, right = statuses[num-idx], statuses[num+idx]
                if left == right:
                    statuses[num-idx] = switch(left)
                    statuses[num+idx] = switch(right)
                else:
                    break
                idx += 1
    
    for j in range(1,n+1):
        print(statuses[j], end = ' ')
        if not j % 20:
            print()
    print()


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    statuses = [0] + list(map(int, input().split()))
    m = int(input())
    students = [list(map(int, input().split())) for _ in range(m)]
    solution(n, statuses, m, students)
