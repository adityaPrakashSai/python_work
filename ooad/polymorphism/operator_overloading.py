# operators can be overloaded to operate in certain user defined way. the operator acts differently for different data types

# Java and javascript do not support operator overloading
class ComplexNumber:
    def __init__(self):
        self.real = 0
        self.imaginary = 0
    
    def set_value(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, c):
        result = ComplexNumber()
        result.real = self.real + c.real
        result.imaginary = self.imaginary + c.imaginary
        return result
    
    def display(self):
        print("(", self.real, "+", self.imaginary, "i)")

c1 = ComplexNumber()
c1.set_value(11, 5)
c2 = ComplexNumber()
c2.set_value(2, 6)
c3 = ComplexNumber()
c3 = c1 + c2
c3.display()
