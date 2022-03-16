def staircase(n):
    nv = n
    tv = 1
    for i in range(n):
        print (('#' * tv).rjust(nv, ' '))
        tv += 1


print (staircase(5))