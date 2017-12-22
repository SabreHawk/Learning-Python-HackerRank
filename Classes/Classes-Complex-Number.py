import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        return Complex(self.real+other.real,self.imaginary+other.imaginary)
    def __sub__(self, other):
        return Complex(self.real-other.real,self.imaginary-other.imaginary)
    def __mul__(self, other):
        temp_real = self.real*other.real-self.imaginary*other.imaginary
        temp_imag = self.real*other.imaginary + self.imaginary *other.real
        return Complex(temp_real,temp_imag)
    def __truediv__(self, other):
        temp_real = (self.real*other.real+self.imaginary*other.imaginary)/(pow(other.real,2)+pow(other.imaginary,2))
        temp_imag = (self.imaginary*other.real - self.real*other.imaginary)/(pow(other.real,2)+pow(other.imaginary,2))
        return Complex(temp_real,temp_imag)
    def mod(self):
        return Complex(pow(self.real**2+self.imaginary**2, 0.5), 0.0)
    def __str__(self):
         return '{0:.2f}{1:+.2f}i'.format(self.real, self.imaginary)

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')