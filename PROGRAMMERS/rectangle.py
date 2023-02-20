# # 직사각형 만들기
# # [[1,3],[4,3],[4,10]] -> print(직사각형만드는 좌표)
# from collections import Counter

# def solution(array):
    
#     for i in zip(*v):
#         count = Counter(i)
#         answer.extend([j for j in count if count[j] == 1])

#     print(answer)

#     return answer

## palindrome
def solution(s):
    result = 0
    for i in range(len(s)//2):
        j = len(s)-1-i
        if s[i] != s[j]:
            return -1
    return 1

print(solution('abcd'))
print(solution('aaba'))
print(solution('a'))