'''
https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

- 0: 상류, 1: 하류
- B[i] = 1, B[i+1] = 0일 때, A 비교
- A[i] > A[i+1], i eats i+1
- A[i] < A[i+1], i+1 eats i
- while문 끝나고 stack에 아무것도 없으면 해당 물고기는 살아남은 것
'''

def solution(A, B):
    stack = []
    answer = 0

    for i in range(len(A)):
        if B[i] == 1:
            stack.append(A[i])
            continue
        
        while stack:
            if stack[-1] < A[i]:
                stack.pop()
            else:
                break
        
        if not stack:
            answer += 1

    answer += len(stack)
    return answer