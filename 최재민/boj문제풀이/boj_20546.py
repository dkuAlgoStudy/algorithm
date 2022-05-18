import copy

money = int(input())
money1 = copy.deepcopy(money)
stock = 0
stock1 = 0

long = 0
short = 0

day = list(map(int, input().split()))

for i in range(14):
    if money1 >= day[i]:
        stock1 += money1 // day[i]
        money1 = money1 % day[i]

for i in range(13):

    if day[i] > day[i+1]:
        long = 0
        short += 1
        if short >= 3:
            stock += money // day[i+1]
            money = money % day[i+1]
    elif day[i] < day[i+1]:
        short = 0
        long += 1
        if long >= 3:
            money += stock * day[i+1]
            stock = 0
    else:
        short, long = 0, 0

if money+stock*day[13] < money1+stock1*day[13]:
    print("BNP")
elif money+stock*day[13] == money1+stock1*day[13]:
    print("SAMESAME")
else:
    print("TIMING")
