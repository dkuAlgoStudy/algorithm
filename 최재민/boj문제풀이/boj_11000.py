import heapq
import sys

n = int(input())

timetable = []
for _ in range(n):
    timetable.append(list(map(int, sys.stdin.readline().split())))

timetable = sorted(timetable, key = lambda x : x[0])

q = []

for i, j in timetable:
    if q and q[0] <= i:
        heapq.heappop(q)
    heapq.heappush(q, j)
print(len(q))
