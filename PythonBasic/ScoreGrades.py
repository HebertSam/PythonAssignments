import random


def scoreGrades ():
    

    for i in range(6):
        
        grade = random.randint(59, 101)

        if grade >= 60 and grade < 70:
            print "score:", grade, "; Your grade is a D"
        elif grade >= 70 and grade < 80:
            print "score:", grade, "; Your grade is a C"
        elif grade >= 80 and grade < 90:
            print "score:", grade, "; Your grade is a B"
        else:
            print "score:", grade, "; Your grade is an A"
    print "End of the program. Bye!"

scoreGrades()