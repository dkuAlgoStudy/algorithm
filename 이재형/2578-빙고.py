def bingoCheck(ans):
    binNum = 0
    sumDiagonalLeft = 0
    sumDiagonalRight = 0
    for i in range(5):
        sumWidth = 0
        sumHeight = 0
        sumDiagonalLeft += ans[i][i]
        sumDiagonalRight += ans[i][4-i]
        for j in range(5):
            sumHeight += ans[j][i]
            sumWidth += ans[i][j]
        if sumWidth == 5:
            binNum += 1
        if sumHeight == 5:
            binNum += 1
    if sumDiagonalLeft == 5:
        binNum += 1
    if sumDiagonalRight == 5:
        binNum += 1

    return binNum
  

if __name__ == "__main__":
    binNum = 0
    arr = []
    t = 0 
    count = 0
    ans = [[0]*5 for _ in range(5)]
    
    bingo = [list(map(int, input().split())) for _ in range(5)]
    for i in range(5):
        arr.extend(list(map(int, input().split())))

    for a in arr:
        flag = True
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == a:
                    count += 1
                    ans[i][j] = 1
                    binNum = bingoCheck(ans)
                    if binNum >= 3:
                        print(count)
                        exit()
                    flag = False
            if flag == False:
                break
