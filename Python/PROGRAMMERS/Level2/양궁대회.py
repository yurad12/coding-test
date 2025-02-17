# https://school.programmers.co.kr/learn/courses/30/lessons/92342

def solution(n, info):
    def dfs(ryan, idx, count, score):
        nonlocal max_diff, answer
        
        if count == 0 or idx > 10:
            apeach = sum([10-i for i in range(11) if (info[i] >= ryan[i] and info[i] != 0)])
            diff = score - apeach
            # print(ryan, score, apeach, diff)
            if diff > max_diff:
                max_diff = diff
                answer = ryan[:]
            elif diff == max_diff:
                for i in range(10, -1, -1):
                    if ryan[i] > answer[i]:
                        answer = ryan[:]
                        break
                    elif ryan[i] < answer[i]:
                        break
            return
        
        dfs(ryan, idx+1, count, score)
        
        if count >= info[idx] + 1:
            ryan[idx] = info[idx] + 1
            dfs(ryan, idx+1, count-info[idx]-1, score+10-idx)
            ryan[idx] = 0
            
        if idx == 10:
            ryan[idx] += count
            dfs(ryan, idx+1, 0, score)
            ryan[idx] -= count
    
    max_diff = 0
    answer = [0] * 11
    dfs([0] * 11, 0, n, 0)

    if max_diff == 0:
        answer = [-1]
    
    return answer