def drawStars(x):
    for i in range(len(x)):
        star = ""
        for j in range(x[i]):
            star += "*"
        print star

a = [1,2,3,4]

drawStars(a)

def drawStars2 (x):
    for i in range(len(x)):
        star = ''
        if type(x[i]) == str:
            for j in range(len(x[i])):
                star += x[i][0]
        elif type(x[i]) == int:
            for k in range(x[i]):
                star += "*"
        print star

b = [3, "Jack", 4, "Ben", 2]

drawStars2(b)
                