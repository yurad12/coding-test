# https://school.programmers.co.kr/learn/courses/30/lessons/12941

### solution1
def find_min_value(array1, array2):
    sum_value = 0
    for i in range(len(array1)):
        sum_value += (array1[i] * array2[len(array1)-i-1])
    return sum_value

def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()
    
    if A[0] < B[0]:
        answer = find_min_value(A,B)
    else:
        answer = find_min_value(B,A)

    return answer


### solution2
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += (A[i] * B[i])
    return answer