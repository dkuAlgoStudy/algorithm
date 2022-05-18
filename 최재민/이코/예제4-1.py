N = int(input())

x,y=1,1
move = input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
nx=0
ny=0

for i in move:
    for j in range(4):
        if i == 'L':
            nx = x+dx[0]
            ny = y+dy[0]
        elif i == 'R':
            nx = x+dx[1]
            ny = y+dy[1]
        elif i == 'U':
            nx = x+dx[2]
            ny = y+dy[2]
        elif i == 'D':
            nx = x+dx[3]
            ny = y+dy[3]
    if nx<1 or ny<1 or nx>N or ny>N:
        continue

    x,y = nx,ny

print(x,y)
