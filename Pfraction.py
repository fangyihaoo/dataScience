from fractions import Fraction
class PFraction(Fraction):
    def __str__(self):
        n = self.numerator
        d = self.denominator
        i = n // d
        int_str = f'{i} ' if i else ''
        n = n % d
        n_str = f'{n}/{d}' if n else ''
        return int_str + n_str
    
    def __add__(self, other):
        return PFraction(Fraction.__add__(self, other))
if __name__ == '__main__':
    f1 = PFraction(3, 5)
    f2 = PFraction(1, 2)
    f3 = f1 + f2
    print(f3)
    f4 = Fraction(3, 5)
    f5 = Fraction(1, 2)
    f6 = f4 + f5
    print(f6)