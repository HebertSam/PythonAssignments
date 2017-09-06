a = ["magical unicorns", 19, "hello", 98.98, "world"]
b = [2, 3, 1, 7, 4, 12]
c = ["magical", "unicorns"]

def types(x):
    sum = 0
    string = ""
    for i in range(0, len(x)):
        if type(x[i]) == int or type(x[i]) == float:
            sum += x[i]
        elif type(x[i]) == str:
            string += x[i]
    if sum != 0 and string != "":
        print "the list you entered is of mixed type"
        print "string:", string
        print "sum:", sum
    elif sum != 0 and string == "":
        print "the list you entered in of integer type"
        print "sum:", sum
    elif sum == 0 and string != "":
        print "the list you entered is of string type"
        print "string:", string

types(a)
types(b)
types(c)