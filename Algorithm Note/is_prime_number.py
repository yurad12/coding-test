import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
    
print(is_prime_number(4)) # False
print(is_prime_number(7)) # True