import sys

T = int(input())

for _ in range(T):
    N = int(int(input()))
    list1 = list(map(int, sys.stdin.readline().split()))
    print(min(list1), max(list1))
