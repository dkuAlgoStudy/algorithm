t = int(input())


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


for _ in range(t):
    n, m = map(int,input().split())
    print(factorial(m)//(factorial(m-n)*factorial(n)))