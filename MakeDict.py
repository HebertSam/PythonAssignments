name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makeDict (x, y):
    newDict = {}
    if len(x) > len(y):
        for i in range(len(x)):
            newDict[x[i]] = y[i]
    else:
        for i in range(len(y)):
            newDict[y[i]] = x[i]
    return newDict

print makeDict(name, favorite_animal)