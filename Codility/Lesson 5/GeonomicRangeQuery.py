'''
https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

- n^2으로 풀면, 시간 초과남
- 접두사를 이용해서 문자열 내의 해당 인덱스까지 각 문자가 몇 번 들어가 있는지를 계산
- 그리고 q위치의 해당 접두사 개수와 p위치의 개수의 차를 구하면 문자가 들어 있는지 확인할 수 있음
- 이렇게 하면 시간복잡도: O(n+m)
'''

def solution(S, P, Q):
    n, m = len(S), len(P)
    pre_A = [0] * (n+1)
    pre_C = [0] * (n+1)
    pre_G = [0] * (n+1)
    pre_T = [0] * (n+1)
    
    for i in range(1,n+1):
        pre_A[i] = pre_A[i-1] + (1 if S[i-1] == 'A' else 0)
        pre_C[i] = pre_C[i-1] + (1 if S[i-1] == 'C' else 0)
        pre_G[i] = pre_G[i-1] + (1 if S[i-1] == 'G' else 0)
        pre_T[i] = pre_T[i-1] + (1 if S[i-1] == 'T' else 0)


    answer = []
    for i in range(m):
        p, q = P[i], Q[i]+1

        if pre_A[q] - pre_A[p] > 0:
            answer.append(1)
        elif pre_C[q] - pre_C[p] > 0:
            answer.append(2)
        elif pre_G[q] - pre_G[p] > 0:
            answer.append(3)
        else:
            answer.append(4)
