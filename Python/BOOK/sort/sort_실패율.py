# https://www.programmers.co.kr/learn/courses/30/lessons/42889
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 4
# stages = 	[4,4,4,4,4]

def solution(N, stages):
    stages = sorted(stages)
    current = [0] * (N+2)
    
    for stage in stages:
        current[stage] += 1
    # print(current)
    
    answer = {}
    for i in range(1,N+1):
        if current[i] == 0:
            answer[i]=0
        else:
            temp = current[i] / sum(current[i:])
            answer[i]=temp
    answer = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    answer = [x[0] for x in answer]
    return answer

print(solution(N,stages))