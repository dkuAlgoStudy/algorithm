now = input()
x = int(now[1])
y = int(ord(now[0]))-int(ord('a'))+1

move = [[-2,-1], [-1,-2], [1,-2], [2, -1], [2,1],[1,2],[-1,2],[-2,1]]

result = 0

for i in move:
    dest_x = x + i[0]
    dest_y = y + i[1]

    if dest_x >= 1 and dest_x <= 8 and dest_y>=1 and dest_y<=8:
        result +=1

print(result)