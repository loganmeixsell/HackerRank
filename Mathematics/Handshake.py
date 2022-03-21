def handshake(n):
    handshaketotal = 0
    for i in range(n-1):
        handshaketotal = handshaketotal + (n-i-1)
        # print(n-i-1)
    return(handshaketotal)

def handshakebetter(n):
    n = n-1
    print(int((n*(n+1))
          /2))

handshakebetter(3)

