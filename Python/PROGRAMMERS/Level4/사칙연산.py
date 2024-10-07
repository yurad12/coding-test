# https://school.programmers.co.kr/learn/courses/30/lessons/1843

def solution(arr):
    nums, ops = [], []
    for i, item in enumerate(arr):
        if not i % 2:
            nums.append(item)
        else:
            ops.append(item)

    n = len(nums)
    INF = int(1e9)
    max_dp = [[-INF]*n for _ in range(n)]
    min_dp = [[INF]*n for _ in range(n)]
    
    for step in range(n):
        for i in range(n-step):
            j = i + step
            if not step:
                max_dp[i][j] = int(nums[i])
                min_dp[i][j] = int(nums[i])
                continue
            for k in range(i,j):
                if ops[k] == "+":
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k]+max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k]+min_dp[k+1][j])
                elif ops[k] == "-":
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k]-min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k]-max_dp[k+1][j])
                
    return max_dp[0][n-1]