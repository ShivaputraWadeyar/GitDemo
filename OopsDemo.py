# classes are user defined blueprint
# sum,multiplication,addition,constant
# methods, class

class Calculator:
    num = 100

    def __init__(self,a,b):
        print("i am in constructor")
        self.first=a
        self.second=b

    def getData(self):
        print("i am executing method")

    def sum(self):
        return self.first + self.num+self.second


obj = Calculator(3,5)
obj.getData()
print(obj.sum())

obj1 = Calculator(8,3)
obj1.getData()
print(obj1.sum())



