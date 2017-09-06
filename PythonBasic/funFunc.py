def oddEven ():
    for i in range(1, 2001):
        if i % 2 == 0:
            print "number is", i, "This is an even number"
        else:
            print "number is", i, "This is an odd number"
# oddEven()

def mult (a, b):
    for i in range(len(a)):
        a[i] *= b
    return a

# print mult([1,2,3,4])


def layeredMulti (a):
    newarr = []
    for i in range(len(a)):
        temparr = []
        for j in range(a[i]):
            temparr.append(1)
        newarr.append(temparr)

    return newarr

print layeredMulti(mult([1,2,3,4], 3))
        