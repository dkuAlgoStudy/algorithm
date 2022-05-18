n = int(input())

star = [[' ']* (4*n-3)  for _ in range(4*n-3)]

#c_x, c_y = (4*n-3)//2, (4*n-3)//2
x, y = 0, 0

while True:
    if n == 1:
        star[x][y] = '*'
        break

    for i in range(4*n-3):
        star[x][y+i] = '*'
        star[x+i][y] = '*'
        star[x + 4*n - 3 - 1][y+i] = '*'
        star[x+i][y + 4*n - 3 - 1] = '*'

    n -= 1
    x += 2
    y += 2


for i in star:
    temp = ""
    for j in i:
        temp += j
    print(temp)