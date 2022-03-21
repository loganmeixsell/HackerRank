import math
def lowestTriangle(trianglebase, area):
    # Write your code here
    # print(area*2/trianglebase)
    return(math.ceil(area * 2 / trianglebase))
lowestTriangle(17,100)