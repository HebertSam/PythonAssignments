class MathDojo(object):
    def __init__ (self):
        self.total = 0

    def add (self, *args):            
        for i in args:
            if type(i) == list or type(i) == tuple:
                temp = 0
                
                for j in i:
                    temp += j
                self.total += temp
                continue
            self.total += i
        return self
    
    def sub(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                temp = 0
                for j in i:
                    temp += j
                self.total += temp
                continue
            self.total -= i
        return self

    def results(self):
        print self.total

mc = MathDojo()

mc.add([1], 3, 4).add([3,5,7,8], [2,4,1.25]).sub(2, [2,3], [1.1,2.3]).results()
