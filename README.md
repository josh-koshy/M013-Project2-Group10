# M013-Project2

#Explore Only
import random
def explore():
    sum1, sum2, sum3 = 0, 0, 0
    for i in range(100):
        sum1 = sum1 + random.normalvariate(9, 3)
        sum2 = sum2 + random.normalvariate(7, 5)
        sum3 = sum3 + random.normalvariate(11, 7)
    return sum1 + sum2 + sum3

print(explore())
