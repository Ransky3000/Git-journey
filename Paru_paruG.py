def butterfly(n):
    heigth = 2*n
    width = heigth + 3
    isSlash = False
    isBackSlash = False

    for row in range(heigth):
        print("(",end="")
        for col in range(width):
            if row < n:
                if col == width-1: print(")")
                elif (col + row) == (width - 2): isSlash = True, print("/",end="")
                elif (row > 0 and col <= (width - 2)) and isSlash:print(".",end="")
                elif (n-1) == row and (width//2) == col:print("G",end="")
                elif (row + 1) == col: isBackSlash = True,print("\\",end="")
                elif (row > 0 and col > 0) and not(isBackSlash) and col < (width//2) - 1:print(".",end="")
                elif isBackSlash:print(" ",end="")
            else:
                if col == width-1: print(")")
                elif (col <= (n-2)-(row-n))  and (row < heigth-1): print(".",end="")
                elif (col + row) == heigth: isSlash = True, print("/",end="")
                elif col <= n and isSlash: print(" ",end="")
                elif col == (width//2): print("|",end="")
                elif (row >= n+1) and (col > n+1) and col <= (n+1)+(row-n): print(" ",end="")
                elif (row+2) == col: isBackSlash = True, print("\\",end="")
                elif (row >= n) and (col > n+2) and col <= (width-2): print(".",end="")
        isSlash = isBackSlash = False

butterfly(int(input("Enter n: ")))