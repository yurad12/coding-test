'''
https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog/
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A)
    fibo = [1,1]
    while fibo[-1] < n+2:
        fibo.append(fibo[-1]+fibo[-2])

    A.append(1)
    jumps = [-1] * (n+2)
    jumps[0] = 0
    for i in range(n+1):
        if not A[i]:
            continue
        for f in fibo:
            prev = i - f
            if prev < -1:
                break
            if jumps[prev+1] == -1:
                continue
            if jumps[i+1] == -1 or jumps[i+1] > jumps[prev+1]+1:
                jumps[i+1] = jumps[prev+1] + 1

    return jumps[n+1]