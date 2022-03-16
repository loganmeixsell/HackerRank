listcheck = [-3,-2,-1,0,1,2]





def plusMinus(arr):
    total = 0
    pos = 0
    zero = 0
    neg = 0
    for x in arr:
        total += 1
        if x < 0:
            neg += 1
        elif x == 0:
            zero += 1
        elif x > 0:
            pos += 1
    neg = neg/total
    zero = zero/total
    pos = pos/total
    listfinal = [pos,neg,zero]
    return listfinal         

okok = plusMinus(listcheck)
print(okok)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)