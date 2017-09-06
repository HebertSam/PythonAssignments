def multiTable():

    for i in range(13):
        if i == 0:
            print "x 1 2 3 4 5 6 7 8 9 10 11 12"
        else:
            row = ""
            for j in range(1, 13):
                temp = i * j
                row += str(temp)
                row += " "
            print i, row
    

multiTable()