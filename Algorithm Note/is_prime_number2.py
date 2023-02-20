import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n+1)]
array[0] = False # 1은 소수가 아니니까

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        # i를 제외한 i의 모든 배수 지우기
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n+1): # 3에서 16까지이면 range(3,17)로 조정
    if array[i]:
        print(i, end=' ')