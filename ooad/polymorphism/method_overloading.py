# method overloading helps to achieve static polymorphism
# methods are overloaded if a class has more than one method with the same name, 
# but either the number of arguments is different or the type of arguments is different.

class Sum:
    def addition(self, a, b, c = 0):
        return a + b + c

sum = Sum()
print(sum.addition(14, 35))
print(sum.addition(31, 34, 43))

