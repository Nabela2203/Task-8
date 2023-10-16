# Using Python Oops. Kindly complete the following task.
# 1. Create a python class called Circle with constructor which will take a list as an argument for the task.
# The list is [10, 501, 22, 37, 100, 999, 87, 351]

l1 = [10, 501, 22, 37, 100, 999, 87, 351]
class circle:
    # __init__ - constructor operator - whenever we call the name of the class - this operator executes
    # self - first parameter act as a default parameter
        def __init__(self,l1):
            self.l1 = l1
        def print_list(self):
            print(self.l1)
obj = circle(l1)
obj.print_list()