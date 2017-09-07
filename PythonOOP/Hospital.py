class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bedNum = None
        

    def patInfo (self):
        print self.name
        print self.bedNum

class Hospital(object):
    def __init__(self, namehosp, cap):
        self.namehosp = namehosp
        self.cap = cap
        self.patents = []
        self.bed = 0
    

    def admit(self, patient):
        if len(self.patents) < self.cap:
            self.patents.append(patient)
            self.bed += 1
            patient.bedNum = self.bed
            print "You have been admitted"
        else:
            print "Sorry the hospital is full"

        return self

    def discharge(self, patName):
        for i in self.patents:
            if patName == i.name:
                self.patents.remove(i)
                i.bedNum = None
        self.bed -= 1
        return self

    def info(self):
        print self.cap
        print len(self.patents)


bobs = Hospital("Bob's Hospital", 5)



pat1 = Patient(1, "Greg", "bees")
pat2 = Patient(2, "Sam", "bears")
pat3 = Patient(3, "Seth", "beats")
pat4 = Patient(4, "Dan", "cow")
pat5 = Patient(5, "Ray", "cheese")
pat6 = Patient(6, "Devi", "mice")


bobs.admit(pat1).admit(pat2).admit(pat3).admit(pat4).admit(pat5).admit(pat6).discharge("Ray").admit(pat6).info()
pat3.patInfo()
pat5.patInfo()
pat6.patInfo()