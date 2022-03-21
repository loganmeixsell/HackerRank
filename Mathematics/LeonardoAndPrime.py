def primeCount(n):
    totalprimes = []
    # Write your code here
    if n >2:
        for numloop in range (2,n+1):
            notprime = False
            for i in range(2,numloop):
                if numloop % i == 0:
                    notprime = True
                    break
            if notprime:
                pass
            else:
                totalprimes.append(int(numloop))
                result = 1
                for x in totalprimes:
                    result = result * x
                if result > n:
                    return(len(totalprimes)-1)
                    break
    elif n == 1:
        return(0)
    else:
        return(1)


primeCount(1)