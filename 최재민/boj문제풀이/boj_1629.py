import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())


def cal(a, b):
    if b == 1:
        return a % C
    temp = cal(a, b//2)

    if b % 2 == 0:
        return temp * temp % C
    else :
        return temp * temp * a % C

print(cal(A,B))