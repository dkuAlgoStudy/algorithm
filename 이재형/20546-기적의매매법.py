def BNP(arr,money):
    count= 0
    for i in range(14):
        while True:
            if money < arr[i]:
                break
            count += 1
            money -= arr[i]
            if money < arr[i]:
                break
    return money,count

def timing(arr,money):
    count = 0
    for i in range(11):
        if arr[i] < arr[i+1] and arr[i+1] < arr[i+2] and arr[i+2] < arr[i+3]:
            money = (count*arr[i+3]) + money   
            count = 0
        elif arr[i] > arr[i+1] and arr[i+1] > arr[i+2] and arr[i+2] > arr[i+3]:
            while True:
                if money < arr[i+3]:
                    break
                count += 1
                money -= arr[i+3]
                if money < arr[i+3]:
                    break
    return money,count

n = int(input())
arr = list(map(int, input().split()))
sum_b = 0
sum_t = 0

bnp_m, bnp_c = BNP(arr,n)
timing_m, timing_c = timing(arr,n)

sum_b = (arr[13]*bnp_c)+bnp_m
sum_t = (arr[13]*timing_c)+timing_m

if sum_t == sum_b:
    print("SAMESAME")
elif sum_t > sum_b:
    print("TIMING")
else:
    print("BNP")
