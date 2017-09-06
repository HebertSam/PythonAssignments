def compLists(x, y):
    if len(x) != len(y):
        print "the lists are not the same"
    else:
        for i in range(0, len(x)):
            if x[i] != y[i]:
                print "the lists are not the same"
                break
            elif i == len(x) - 1:
                print "the lists are the same"
    
   


list1 = [1,2,5,6,2]
list2 = [1,2,5,6,2]
list3 = [1,2,5,6,2,3]
list4 = [1,2,5,6,2,16]
list5 = ['celery','carrots','bread','milk']
list6 = ['celery','carrots','bread','cream']

compLists(list1, list2)
compLists(list2, list3)
compLists(list4, list2)
compLists(list5, list6)