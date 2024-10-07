import sys
input = sys.stdin.readline

def solution(arr):
    n = len(arr)
    arr.sort()
    rearranged_arr = sorted(arr)
    count = 0
    start, end = 0, 0

    while start < n and end < n:
        if arr[start] < rearranged_arr[end]:
            count += 1
            start += 1
            end += 1
        else:
            end += 1
    
    return count

print(solution([1, 3, 5, 2, 1, 3, 1])) # 4
print(solution([1, 2, 6, 3, 2, 1])) # 4