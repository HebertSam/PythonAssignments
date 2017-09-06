import random

def coinToss ():
    heads = 0
    tails = 0

    for i in range(1, 5001):
        toss = round(random.random())

        if toss == 1:
            heads += 1
            print "attempt # {0} ... throwing a coin ... its heads! ... got {1} head(s) and {2} tails(s) so far".format(i, heads, tails) 
        elif toss == 0:
            tails += 1
            print "attempt # {0} ... throwing a coin ... its tails! ... got {1} head(s) and {2} tails(s) so far".format(i, heads, tails)

coinToss()    