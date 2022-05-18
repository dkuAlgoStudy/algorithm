import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = []
state = [0,0,0]  #상하,좌우,시계방향회전 

for i in range(n):
    arr.append(list(map(int, input().split())))



