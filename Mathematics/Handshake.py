def handshake(n):
    handshaketotal = 0
    for i in range(n-1):
        handshaketotal = handshaketotal + (n-i-1)
        # print(n-i-1)
    return(handshaketotal)


handshake(2)

