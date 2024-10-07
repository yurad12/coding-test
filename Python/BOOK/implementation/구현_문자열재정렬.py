string = input()
string = sorted(string)
alpha = []; num = 0

for i in range(len(string)):
    if string[i].isalpha():
        alpha.append(string[i])
    else:
        num += int(string[i])
    #print(alpha, num)
alpha = ''.join(alpha)
print(alpha+str(num))