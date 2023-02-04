# 모범답안
n = int(input())
count = 0
coin_types = [500,100,50,10]

for coin in coin_types:
    count += n // coin
    n %= coin
print(count)


# 내가 푼 것
cash = int(input())
cnt = 0

while(cash != 0):
    if cash >= 500:
        cnt = cnt + (cash//500)
        cash = cash%500
    elif 100 <= cash < 500:
        cnt = cnt + (cash//100)
        cash = cash%100
    elif 50 <= cash < 100:
        cnt = cnt + (cash//50)
        cash = cash%50
    else:
        cnt = cnt + (cash//10)
        cash = cash%10
    #print('cash:', cash)
    #print('cnt', cnt)
print(cnt)
