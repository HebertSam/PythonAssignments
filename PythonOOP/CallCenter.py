class Call (object):
    def __init__(self, name, number, time, reason, id):
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
        self.id = id

    def display(self):
        print "Name:", self.name
        print "Number:", self.number
        print "Time:", self.time
        print "reason:", self.reason
        print "id:", self.id
    def __repr__(self):
        return "{}, {}, {}".format(self.name, self.time, self.id)

class callCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.size = len(self.calls)
    
    def add (self, *call):
        for i in call:
            self.calls.append(i)
        self.size = len(self.calls)
        return self

    def remove (self):
        self.calls.pop(0)
        self.size = len(self.calls)
        return self

    def remove_by_number (self, number):
        for i in self.calls:
            if i.number == number:
                self.calls.remove(i)

        self.size = len(self.calls)
        return self

    def sort(self):
        self.calls = sorted(self.calls, key=lambda  call: call.time)
        return self

    def info (self):
        for i in self.calls:
            print i.name
            print i.number
            print i.time
        print self.size



call_1 = Call("Bob", "(555) 555-5555", 12, "angry", "1")
call_2 = Call("Jill", "(703) 555-5555", 9, "happy", "2")
call_3 = Call("Sam", "(555) 555-5555", 8, "angry", "3")
call_4 = Call("Ray", "(555) 569-5555", 13, "happy", "4")
call_5 = Call("Gary", "(555) 555-5555", 14, "angry", "5")


center = callCenter([call_1])

center.add(call_2, call_3, call_4,call_5)
center.sort().info()

