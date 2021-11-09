#eGreedy
import random

c1 = [random.normalvariate(9, 3)]
c2 = [random.normalvariate(7, 5)]
c3 = [random.normalvariate(11, 7)]

def bestCaf() -> int:
    c1TA = sum(c1) / len(c1)
    c2TA = sum(c2) / len(c2)
    c3TA = sum(c3) / len(c3)
    if c1TA > c2TA and c1TA > c3TA:
        return 1
    elif c2TA > c1TA and c2TA > c3TA:
        return 2
    else:
        return 3

def eGreedy(e: int) -> float:
    sum = 0
    for i in range(297):
        percent = random.random()
        if percent < e/100:
            i = random.randint(1, 3)
            if i == 1:
                h = random.normalvariate(9, 3)
                sum += h
                c1.append(h)
            elif i == 2:
                h = random.normalvariate(7, 5)
                sum += h
                c2.append(h)
            else:
                h = random.normalvariate(11, 7)
                sum += h
                c3.append(h)
        else:
            if bestCaf() == 1:
                h = random.normalvariate(9, 3)
                sum += h
                c1.append(h)
            elif bestCaf() == 2:
                h = random.normalvariate(7, 5)
                sum += h
                c2.append(h)
            else:
                h = random.normalvariate(11, 7)
                sum += h
                c3.append(h)
    return sum
