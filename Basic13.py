def count ():
    for i in range(1, 256):
        print i


def sum ():
    total = 0
    for i in range(256):
        total += i
        print i
        print total

def max (arr):
    print max(arr)

def oddsarr ():
    arr = []
    for i in range(1, 256 ,2)
        arr.append(i)

def countgreater (arr, Y):
    count = 0
    for i in arr:
        if i > Y:
            count++
    print count

def MaxMinAvg(arr):
    sum = 0
    max = max(arr)
    min = min(arr)

    for i in arr:
        sum += i

    print (max, min, sum/len(arr))

def swapStr (arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = "dojo"
    print arr

def odds():
    for i in range(1, 256, 2):
        print i

def val (arr):
    for i in arr:
        print i

def avg(arr):
    sum = 0
    for i in arr:
        sum += i

    print sum/len(arr)

def sqr (arr):
    for i in range(len(arr)):
        arr[i] = arr[i]**2

    print arr

def zeros (arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    print arr

def shift (arr):
    for i in range(len(arr)):
        arr[i] = arr[i + 1]
    arr[-1] = 0
    
