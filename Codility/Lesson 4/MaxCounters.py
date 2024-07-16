'''
https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
'''

def solution(N, A):
    counts = [0] * (N+1)
    now, max_value = 0, 0

    for a in A:
        if 0 < a and a < N+1:
            if counts[a] < now:
                counts[a] = now
            counts[a] += 1
            if counts[a] > max_value:
                max_value = counts[a]
        else:
            now = max_value

    for i in range(1,N+1):
        if counts[i] < now:
            counts[i] = now

    return counts[1:]