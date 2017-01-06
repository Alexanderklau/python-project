__metaclass__=type

class Person:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print('Hello! im %s' % self.name)

