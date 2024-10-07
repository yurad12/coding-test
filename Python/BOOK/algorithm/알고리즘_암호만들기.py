from itertools import combinations

l, c = map(int, input().split())
char = [i for i in input().split()]
char = sorted(char)
result = list(combinations(char,l))
# last = char[l-1]
#print(result)
for password in result:
    v=0 #모음개수
    # if password[0]==last:
    #     break
    for j in password:
        if j in ['a','e','i','o','u']:
            v += 1
    if (v>=1) & (l-v>=2):
        print(''.join(password))

# a t c i s w
# a c i s t w