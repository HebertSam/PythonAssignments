my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}

def dictTup(x):
    arr = []
    for key, value in x.iteritems():
        temp = (key, value)
        arr.append(temp)

    return arr

print dictTup(my_dict)