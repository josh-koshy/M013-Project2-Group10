from exploitOnlyFinal import *
from exploreOnly import *

def Simulation(t: int):
    print("\nData after " + str(t) + " trials..\n")
    print("Exploit only:")
    oH = 300 * 11
    print("Optimum Happiness -> " + str(oH))
    if findBestCaf() == 1:
        eTH = 9 + 7 + 11 + (297 * 9)
    if findBestCaf() == 2:
        eTH = 9 + 7 + 11 + (297 * 7)
    if findBestCaf() == 3:
        eTH = 9 + 7 + 11 + (297 * 11)
    # eTH -> expected total happiness
    print("Expected Total Happiness -> " + str(eTH))
    regret = oH - eTH
    print("Expected Regret -> " + str(regret))
    totalHappiness = 0
    totalRegret = 0
    for i in range(t):
        h300 = exploit()
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
        h300 = explore()
        totalHappiness = totalHappiness + h300
        regret = oH - h300
        totalRegret = totalRegret + regret
    avgTH = totalHappiness / t  # avgTH -> average total happiness
    print("Average Total Happiness -> " + str(avgTH))
    avgRegret = totalRegret / t
    print("Average Regret -> " + str(avgRegret))

    print("\neGreedy:")

Simulation(1000)
Simulation(10000)
Simulation(100000)
