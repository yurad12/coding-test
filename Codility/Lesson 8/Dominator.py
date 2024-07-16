'''
https://app.codility.com/programmers/lessons/8-leader/dominator/

- Boyer-Moore Voting Algorithm은 시간복잡도가 O(N)
- 후보 선정
    - candidate는 현재까지 과반수 후보를 저장
    - count는 후보의 출현 빈도를 추적
    - 배열을 순회하면서 `count`가 0일 때 새로운 후보를 설정합니다. 후보와 같은 요소가 나오면 `count`를 증가시키고, 다른 요소가 나오면 `count`를 감소
    - 이 과정을 통해 최종적으로 `candidate`가 과반수 후보로 설정됨
- 후보 검증
    - 배열을 다시 순회하여 후보가 실제로 과반수인지 확인
    - 후보의 출현 빈도를 세고, 이 빈도가 전체 요소의 절반 이상인지 확인
    - 과반수이면 후보의 인덱스를 반환하고, 그렇지 않으면 -1을 반환
'''

def solution(A):
    count = 0
    num = None
    for a in A:
        if count == 0:
            num = a
            count = 1
        elif num == a:
            count += 1
        else:
            count -= 1
    
    count = 0
    idx = -1
    for i, a in enumerate(A):
        if a == num:
            count += 1
            idx = i
    
    if count > len(A)//2:
        return idx
    return -1