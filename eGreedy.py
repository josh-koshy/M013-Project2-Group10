#eGreedy
import random

d1 = random.normalvariate(9, 3)
d2 = random.normalvariate(7, 5)
d3 = random.normalvariate(11, 7)
newList = [d1, d2, d3]


def bestCaf() -> int:
    maxVal = 0
    maxIndex = 0
    for i in range(len(newList)):
        if maxVal < newList[i]:
            maxVal = newList[i]
            maxIndex = i
    return maxIndex + 1

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
