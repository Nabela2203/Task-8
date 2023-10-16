# 2. Create proper member variables inside the task if required and use them when necessary. For example for this task
# create a class private variable named pi=3.141

class A:
    def __init__(self,pi):
        self.pi = pi
    def private(self): # private class - use under parent class - local
        print(self.pi)
obj = A(3.141)
obj.private()