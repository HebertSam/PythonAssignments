def findReplace():

    words = "It's thanksgiving day. It's my birthday, too"
    print words.find("day")
    print words.replace("day", "month")


arr = [19,2,54,-2,7,12,98,32,10,-3,6]

def maxMin (arr):
    print(max(arr))
    print(min(arr))

def firstLast (arr):
    newarr = []
    newarr.append(arr[0])
    newarr.append(arr[len(arr)-1])
    print newarr

def newList(arr):
    arr.sort()
    x = arr[:len(arr)/2]
    y = arr[len(arr)/2:]
    y.insert(0, x)
    print y

findReplace()
maxMin(arr)
firstLast(arr)
newList(arr)
