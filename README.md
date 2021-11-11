# M013-Project2-Group10

#eGreedy portion
def eGreedy(e: int):
    sum = 0
    for i in range(297):
        percent = random.random()
        if percent < e/100:
            i = random.randint(1, 3)
            if i == 1:
                h = random.normalvariate(9, 3)
                sum += h
                if h > newList[0]:
                    newList[0] = h
            elif i == 2:
                h = random.normalvariate(7, 5)
                sum += h
                if h > newList[1]:
                    newList[1] = h
            elif i == 3:
                h = random.normalvariate(11, 7)
                sum += h
                if h > newList[2]:
                    newList[2] = h
        else:
            if bestCaf() == 1:
                h = random.normalvariate(9, 3)
                sum += h
                if h > newList[0]:
                    newList[0] = h
            elif bestCaf() == 2:
                h = random.normalvariate(7, 5)
                sum += h
                if h > newList[1]:
                    newList[1] = h
            elif bestCaf() == 3:
                h = random.normalvariate(11, 7)
                sum += h
                if h > newList[2]:
                    newList[2] = h
    return sum
    
    #simulation portion
    
    def Simulation(t: int, e: int): # e is value for e greedy
    print("\nData after " + str(t) + " trials..\n")
    print("Exploit only:")
    oH = 300 * 11 # oH -> optimum happiness
    print("Optimum Happiness -> " + str(oH))
    if findBestCaf() == 1:
        eTH = 9 + 7 + 11 + (297 * 9)
    elif findBestCaf() == 2:
        eTH = 9 + 7 + 11 + (297 * 7)
    elif findBestCaf() == 3:
        eTH = 9 + 7 + 11 + (297 * 11)
    # eTH -> expected total happiness
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
    avgTH = totalHappiness / t # avgTH -> average total happiness
    print("Average Total Happiness -> " + str(avgTH))
    avgRegret = totalRegret / t
    print("Average Regret -> " + str(avgRegret))

    print("\nExplore Only:")
    oH = 300 * 11
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

    print("\neGreedy:")
    oH = 300 * 11
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
