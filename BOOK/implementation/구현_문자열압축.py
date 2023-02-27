# https://school.programmers.co.kr/learn/courses/30/lessons/60057

# 처음 시작한 문자가 다시 돌아올때?
# 같은 문자가 뒤에 있는지 루프
# 같을 때까지 끊고 나머지 더하기
def solution(s):
    answer = []
    if len(s)==1:
        return 1
    
    for i in range(1,len(s)//2+1):
        new_s = ''
        temp = s[:i]
        cnt = 1
        
        for j in range(i,len(s),i):
            if temp == s[j:i+j]:
                cnt += 1
            else:
                if cnt == 1:
                    new_s += temp
                else:
                    new_s += (str(cnt) + temp)
                cnt = 1
                temp = s[j:i+j]
        if cnt == 1:
            new_s += temp
        else:
            new_s += (str(cnt)+temp)
        answer.append(len(new_s))
        #print(new_s, cnt)
        #print(answer)
    #print(answer)
                
    return min(answer)
