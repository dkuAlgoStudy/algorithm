import sys

n = int(input())
village = []

for i in range(n):
    a, people = map(int, sys.stdin.readline().split())
    village.append([a, people])
total = 0
for i in range(n):
    total += village[i][1]
mid = total//2
village = sorted(village)
if total % 2 != 0:
    mid += 1

left = 0

for i in range(n):
    left += village[i][1]
    if left >= mid:
        print(village[i][0])
        break


