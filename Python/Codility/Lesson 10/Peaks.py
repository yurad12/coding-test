'''
https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/

- peak 찾기
- A 사이즈를 역순으로 -1하면서 큰 크기부터 block 사이즈 반복문 돌기, block 사이즈로 나눠떨어지지 않으면 그 크기는 안됨
- peaks를 돌면서 나눈 블럭 안에 peak가 들어 있는지 확인하기
    - peak가 해당 블록안에 있으면 count += 1
    - i가 블록 개수니까 count와 블록 수가 같아지면 그게 답임
'''

def solution(A):
    n = len(A)    
    peaks = []
    for i in range(1,n-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.append(i)
            
    for i in range(n,0,-1):
        if n % i:
            continue
        size = n // i
        block = [0] * i
        count = 0
        for j in range(len(peaks)):
            # 해당 peak가 block의 몇 번째에 해당되는지 확인
            # block에 peak가 있는지 확인할 수 있음
            idx = peaks[j] // size
            if not block[idx]:
                block[idx] = 1
                count += 1
            if count == i:
                return count

    return 0