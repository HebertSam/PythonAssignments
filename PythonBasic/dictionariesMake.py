Sam = {
    "first name": "Sam",
    "age": 28,
    "birth country": "United States",
    "favorite language": "Python"
    }
def bio(x):
    for key, value in x.iteritems():
        print "My {0} is {1}".format(key, value)

    


bio(Sam)