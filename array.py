numlist = [[1,2,3,80],
            [4,5,7,90],
            [8,9,10,100],
            [101,102,103,104]]



def diagonalDifference(arr):
    primarydiagnol = 0
    secondarydiagnol = 0
    finalnum = 0
    for i in range(len(arr)):
        print (f"i is currently {i}")
        primarydiagnol += (arr[i][i])
        secondarydiagnol += (arr[i][-i-1])
    finalnum = abs(primarydiagnol - secondarydiagnol)
    return finalnum