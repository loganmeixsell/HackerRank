def miniMaxSum(arr):
    finallist = []
    arr.sort()
    finallist.append(sum(arr[0:4]))
    finallist.append(sum(arr[1:5]))
    print (f"{finallist[0]} {finallist[1]}")
    print (sum(arr[1:5]))
    


minmax = [4,8,32,54,3]
minmax.sort()