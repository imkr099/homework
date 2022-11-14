class A:
    def __init__(self, vallue):
        self.vallue = vallue
    def __add__(self, other):
        return self.vallue + other.vallue

class B:
    def __init__(self, vallue):
        self.vallue = vallue
    def __sub__(self, other):
        return self.vallue - other.vallue

class C:
    def __init__(self, vallue):
        self.vallue = vallue
    def __mul__(self, other):
        return self.vallue * other.vallue

class D:
    def __init__(self, vallue):
        self.vallue = vallue
    def __truediv__(self, other):
        return self.vallue / other.vallue

class E(A, B, C, D):
    def __init__(self, vallue):
        A.__init__(self, vallue)
        B.__init__(self, vallue)
        C.__init__(self, vallue)
        D.__init__(self, vallue)

num = E(69)
num1 = E(30)

print(f'Add - {num + num1}\n'
      f'Sub - {num - num1}\n'
      f'Mul - {num * num1}\n'
      f'Truediv - {num / num1}\n')