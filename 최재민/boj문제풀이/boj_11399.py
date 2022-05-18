import sys

n = int(input())

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

for i in range(1,n):
    arr[i] += arr[i-1]

print(sum(arr))