# https://www.acmicpc.net/problem/11057

n = int(input())
nums = [0] + [i for i in range(10,0,-1)]
d = [0] * 1001
d[1] = len(nums)-1
d[2] = sum(nums)
for i in range(3,n+1):
    for j in range(1,len(nums)):
        nums[j] = sum(nums[j:])
    d[i] = sum(nums)
print(d[n]%10007)