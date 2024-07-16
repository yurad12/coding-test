'''
https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

- 구간합
길이가 4개부터는 어차피 2와 3개만 해도 최솟값이 되어야 한다.
그러니까 길이가 2, 3인 경우만 확인하면 된다.
'''

INF = int(1e9)

def solution(A):
    answer = 0
    min_avg = INF

    for i in range(len(A)-1):
        avg2 = (A[i]+A[i+1]) / 2
        if avg2 < min_avg:
            min_avg, answer = avg2, i
        
        if i < len(A)-2:
            avg3 = (A[i]+A[i+1]+A[i+2]) / 3
            if avg3 < min_avg:
                min_avg, answer = avg3, i
    
    return answer
