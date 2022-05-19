def findmine(i,j, n, arr):
    sum = 0
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, 1, -1]
    for k in range(8):
        if 0 <= i+dx[k] < n and 0 <= j+dy[k] < n:
            if arr[i+dx[k]][j+dy[k]] == "*":
                sum += 1
        else:
            continue
    return str(sum)
    
def itIsMine(arr, arr1, n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "*":
                arr1[i][j] = "*"
    return arr1

if __name__ == "__main__":
    n = int(input())
    locMine = []
    locClick = []
    ans =[["."]*n for _ in range(n)]

    for _ in range(n):
        locMine.append(list(input()))
    for _ in range(n):
        locClick.append(list(input()))
        
    for i in range(n):
        for j in range(n):
            if locClick[i][j] == 'x':
                ans[i][j] = findmine(i, j, n, locMine)
                if locMine[i][j] == "*":
                    ans = itIsMine(locMine, ans, n)
        
    for i in range(n):
        ansPrint = "".join(ans[i])
        print(ansPrint)
