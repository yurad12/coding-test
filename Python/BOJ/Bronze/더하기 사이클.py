# https://www.acmicpc.net/problem/1110
num = int(input())
num_list = [num]
#cnt = 0

while(len(num_list)==len(set(num_list))):

    if num < 10:
        temp = num
        num = num*10 + temp

    else:
        first = int(num/10)
        second = num%10
        temp = (first+second)%10
        num = (num_list[-1]%10)*10 + temp

    num_list.append(num)
     
print(len(num_list)-1)

#if cnt >10 : break
#    cnt+=1