# https://www.acmicpc.net/problem/20164
import sys
input = sys.stdin.readline

N = list(map(int, input().strip()))

answer = [float('inf'), 0]

def count_odd(nums):
    count = 0
    for i in nums:
        if i % 2 == 1:
            count += 1
    return count

def dfs(nums, now):
    if len(nums) == 1:
        answer[0] = min(answer[0], now)
        answer[1] = max(answer[1], now)
        return
    elif len(nums) == 2:
        new_nums = list(map(int, str(sum(nums))))
        dfs(new_nums, now + count_odd(new_nums))
    else:
        for i in range(1, len(nums)-1):
            a = int(''.join(map(str, nums[:i])))
            for j in range(i+1, len(nums)):
                b = int(''.join(map(str, nums[i:j])))
                c = int(''.join(map(str, nums[j:])))
                new_nums = list(map(int, str(a+b+c)))
                dfs(new_nums, now + count_odd(new_nums))

dfs(N, count_odd(N))
print(answer[0], answer[1])