import sys
from collections import defaultdict
n = int(input())
file = defaultdict(int)

for _ in range(n):
    name, ext = sys.stdin.readline().rstrip().split('.')
    file[ext] += 1

for key, value in sorted(file.items()):
    print(key, value)
