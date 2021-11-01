#Simulation Function
from exploitOnly import *
from exploreOnly import *

def Simulation(t):
    oH = 300*11
    print("Optimum Happiness -> " + str(oH))
    eTH = 9 + 7 + 11 + 297*11 # eTH -> expected total happiness
    print("Expected Total Happiness -> " + str(eTH))
    regret = oH - eTH
    print("Expected Regret -> " + str(regret))
    print("\nData after " + str(t) + " trials:")
    numTrials = 0
    totalHappiness = 0
    totalRegret = 0
    while numTrials != t:
        h = happinessSum()
        totalHappiness = totalHappiness + h
        regret = oH - h
        totalRegret = totalRegret + regret
        numTrials += 1
    avgTH = totalHappiness / t # avgTH -> average total happiness
    print("Average Total Happiness -> " + str(avgTH))
    avgRegret = totalRegret / t
    print("Average Regret -> " + str(avgRegret))

Simulation(10000)
