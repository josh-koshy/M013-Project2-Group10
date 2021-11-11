import random

#Explore Only
def exploreOnly() -> float:
    sum1, sum2, sum3 = 0, 0, 0
    for i in range(100):
        sum1 = sum1 + random.normalvariate(9, 3)
        sum2 = sum2 + random.normalvariate(7, 5)
        sum3 = sum3 + random.normalvariate(11, 7)
    return sum1 + sum2 + sum3

#Exploit Only
day1 = random.normalvariate(9, 3)
day2 = random.normalvariate(7, 5)
day3 = random.normalvariate(11, 7)

newlist = [day1, day2, day3]

def findBestCaf() -> int:
    maxVal = 0
    maxIndex = 0
    for i in range(len(newlist)):
        if maxVal < newlist[i]:
            maxVal = newlist[i]
            maxIndex = i
    return maxIndex + 1

def exploitOnly() -> float:
    numDays = 3
    sum = day1 + day2 + day3
    while numDays < 300:
        if findBestCaf() == 1:
            sum += random.normalvariate(9, 3)
            numDays += 1
        elif findBestCaf() == 2:
            sum += random.normalvariate(7, 5)
            numDays += 1
        else:
            sum += random.normalvariate(11, 7)
            numDays += 1
    return sum

#eGreedy
def eGreedy(e: int) -> float:
    c1 = random.normalvariate(9, 3)
    c2 = random.normalvariate(7, 5)
    c3 = random.normalvariate(11, 7)
    c1len = 1
    c2len = 1
    c3len = 1
    c1TA = c1
    c2TA = c2
    c3TA = c3
    for i in range(297):
        percent = random.random()
        if percent < e/100:
            i = random.randint(1, 3)
            if i == 1:
                c1len += 1
                h = random.normalvariate(9, 3)
                c1 += h
                c1TA = c1 / c1len
            elif i == 2:
                c2len += 1
                h = random.normalvariate(7, 5)
                c2 += h
                c2TA = c2 / c2len
            else:
                c3len += 1
                h = random.normalvariate(11, 7)
                c3 += h
                c3TA = c3 / c3len
        else:
            if c1TA > c2TA and c1TA > c3TA:
                c1len += 1
                h = random.normalvariate(9, 3)
                c1 += h
                c1TA = c1 / c1len
            elif c2TA > c1TA and c2TA > c3TA:
                c2len += 1
                h = random.normalvariate(7, 5)
                c2 += h
                c2TA = c2 / c2len
            else:
                c3len += 1
                h = random.normalvariate(11, 7)
                c3 += h
                c3TA = c3 / c3len
    return c1 + c2 + c3

#Simulation
def simulation(t: int, e: int): # e is value for e greedy
    oH = 300 * 11  # oH -> optimum happiness
    print("\nData after " + str(t) + " trials..")
    print("\nExplore Only:")
    print("Optimum Happiness -> " + str(oH))
    eTH = 100*9 + 100*7 + 100*11  # eTH -> expected total happiness
    print("Expected Total Happiness -> " + str(eTH))
    regret = oH - eTH
    print("Expected Regret -> " + str(regret))
    totalHappiness = 0
    totalRegret = 0
    for i in range(t):
        h300 = exploreOnly()
        totalHappiness = totalHappiness + h300
        regret = oH - h300
        totalRegret = totalRegret + regret
    avgTH = totalHappiness / t  # avgTH -> average total happiness
    print("Average Total Happiness -> " + str(avgTH))
    avgRegret = totalRegret / t
    print("Average Regret -> " + str(avgRegret))

    print("\nExploit only:")
    print("Optimum Happiness -> " + str(oH))
    eTH = 9 + 7 + 11 + 297 * 11  # eTH -> expected total happiness
    print("Expected Total Happiness -> " + str(eTH))
    regret = oH - eTH
    print("Expected Regret -> " + str(regret))
    totalHappiness = 0
    totalRegret = 0
    for i in range(t):
        h300 = exploitOnly()
        totalHappiness = totalHappiness + h300
        regret = oH - h300
        totalRegret = totalRegret + regret
    avgTH = totalHappiness / t  # avgTH -> average total happiness
    print("Average Total Happiness -> " + str(avgTH))
    avgRegret = totalRegret / t
    print("Average Regret -> " + str(avgRegret))

    print("\neGreedy:")
    print("Optimum Happiness -> " + str(oH))
    eDecimal = e/100
    eTH = (1-eDecimal)*300*11 + (eDecimal/3)*300*9 + (eDecimal/3)*300*7 + (eDecimal/3)*300*11  # eTH -> expected total happiness
    print("Expected Total Happiness -> " + str(eTH))
    regret = oH - eTH
    print("Expected Regret -> " + str(regret))
    totalHappiness = 0
    totalRegret = 0
    for i in range(t):
        h300 = eGreedy(e)
        totalHappiness = totalHappiness + h300
        regret = oH - h300
        totalRegret = totalRegret + regret
    avgTH = totalHappiness / t  # avgTH -> average total happiness
    print("Average Total Happiness -> " + str(avgTH))
    avgRegret = totalRegret / t
    print("Average Regret -> " + str(avgRegret))


simulation(100, 12)
simulation(10000, 12)
simulation(100000, 12)
