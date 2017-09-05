def findChar (x, y):
    newList = []
    for i in x:
        if y in i:
            newList.append(i)
    print newList    


word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'

findChar(word_list, char)
