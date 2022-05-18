n = int(input())

coin = n % 5

if n == 1 or n == 3:
    print('-1')
elif coin == 0 or coin == 2 or coin == 4:
    print(n//5+coin//2)
elif coin == 1 or coin == 3:
    print((n//5-1)+(coin+5)//2)
