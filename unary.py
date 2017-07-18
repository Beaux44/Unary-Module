"""
Creates Unary integer support, includes math, addition, subtraction, multiplication, division, exponents, roots, and logarithms
"""
from math import log

class UnaryError(Exception):
    """Error for when something impossible in unary occurs, may or may not be added upon"""
    pass


class unary:
    """My attempt at making unary numbers work more like regular base-10 integers"""
    symbol = "0"

    def __init__(self, integer):
        if isinstance(integer, str):
            pass
        else:
            raise TypeError("Expected type str, got type %s" % type(integer).__name__)

        self.value = len(integer)
        self.integer = integer
        if self.value>0:
            if self.integer[0] == "-":
                self.value -= self.value*2-1 # I wanted to be special :D
                self.integer = self.integer[1:]

        for i in str(self.integer):
            if i!=unary.symbol:
                raise UnaryError("Unary has only 1 symbol, currently set as %s" % self.symbol)

    def __str__(self):
        return ("-" if self.value < 0 else "") + str(self.integer)

    def __repr__(self):
        return "unary(\"{}\") == {}".format(str(self), str(self.value))

    def __len__(self):
        raise TypeError("object of type 'unary' has no len()")

    def __int__(self):
        return self.value

    def __abs__(self):
        if self.value < 0:
            return str(self)[1:]
        else:
            return str(self)

    def __neg__(self):
        return un(0-self.value)

    def __pos__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == str(other)
        elif isinstance(other, int) or isinstance(other, unary):
            return int(self) == other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, str):
            return str(self) >= str(other)
        elif isinstance(other, int) or isinstance(other, unary):
            return int(self) >= int(other)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, str):
            return str(self) > str(other)
        elif isinstance(other, int) or isinstance(other, unary):
            return int(self) > int(other)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, str):
            return str(self) < str(other)
        elif isinstance(other, int) or isinstance(other, unary):
            return int(self) < int(other)
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, str):
            return str(self) <= str(other)
        elif isinstance(other, int) or isinstance(other, unary):
            return int(self) <= int(other)
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, str):
            return str(self) != str(other)
        elif isinstance(other, int) or isinstance(other, unary):
            return int(self) != int(other)
        else:
            return NotImplemented

    def __add__(self, other):
        x = int(self) + int(other)
        return un(x)

    def __sub__(self, other):
        x = int(self) - int(other)
        return un(x)

    def __mul__(self, other):
        x = int(self) * int(other)
        return un(x)

    def __pow__(self, other):
        x = round(int(self)**(other if isinstance(other, float) else int(other)))
        return un(x)

    def __mod__(self, other):
        x = int(self)%int(other)
        return un(x)

    def __divmod__(self, other):
        return [un(i) for i in divmod(self.value, other)]

    def __floordiv__(self, other):
        x = int(self)//int(other)
        return un(x)

    def __truediv__(self, other):
        x = round(int(self)/int(other))
        return un(x)

def un(n):
    """Returns unary version of base-10 integer"""
    if isinstance(n, int):
        return unary(("-" if n < 0 else "") + unary.symbol*abs(n))
    else:
        raise UnaryError("Expected type integer, got type %s" % type(n).__name__)

def unSum(n, *args):
    """Returns unary sum of any number of given unary strings"""
    for i in args:
        if isinstance(i, unary):
            n+=i
        else:
            raise ValueError("Expected unary value, got %s" % type(i).__name__)
    return un(n)

def unSub(n1, n2):
    """Returns unary absolute value of the difference between two given unary strings"""
    if all([isinstance(n1, unary), isinstance(n2, unary)]):
        return un(n1-n2)
    elif not isinstance(n1, unary):
        raise ValueError("Expected unary value, got %s" % type(n1).__name__)
    else:
        raise ValueError("Expected unary value, got %s" % type(n2).__name__)

def unMul(n, *args):
    """Returns unary product of any number of given unary strings"""
    for i in args:
        if isinstance(i, unary):
            n*=i
        else:
            raise ValueError("Expected unary value, got %s" % type(i).__name__)
    return un(n)

def unDiv(n1, n2):
    """Returns rounded unary qoutient of two given integers"""
    if all([isinstance(n1, unary), isinstance(n2, unary)]):
        return un(round(n1/n2))
    elif not isinstance(n1, unary):
        raise ValueError("Expected unary value, got %s" % type(n1).__name__)
    else:
        raise ValueError("Expected unary value, got %s" % type(n2).__name__)

def unExp(n, p):
    """Returns unary exponent using unExp(n, p) with n to the pth power"""
    if isinstance(n, unary):
        return un(n**p)
    elif not isinstance(n, unary):
        raise ValueError("Expected unary value, got %s" % type(n).__name__)

def unNthRt(n, root):
    """Returns the Nth root of unary string"""
    if isinstance(n, unary):
        return un(round(n**(1/root)))
    else:
        raise ValueError("Expected unary value, got %s" % type(n).__name__)

def unSqrt(n):
    """Returns square root of the given unary string"""
    if isinstance(n, unary):
        return un(n**.5)
    else:
        raise ValueError("Expected unary value, got %s" % type(n).__name__)
def unMod(n1, n2):
    """Returns unary modulo of two given unary strings"""
    assert all([isinstance(n1, unary),isinstance(n2, unary)])
    return un(n1%n2)

def unLog(n, *args):
    """works just like python's normal log function, but works on unary strings, if given a log base, given in base-10"""
    if isinstance(n, unary):
        if len(args) > 1:
            raise TypeError("unLog() takes at most 2 arguments,", len(args)+1, "given.")
        elif len(args) == 1:
            arg = args[0]
            return un(round(log(int(n), arg)))
        else:
            return un(round(log(int(n))))
    elif not isinstance(n, unary):
        raise ValueError("Expected unary value, got %s" % type(n).__name__)

def unLog10(n):
    """Works just like the normal log10 function, but on unary strings"""
    if isinstance(n, unary):
        return un(round(log(int(n), 10)))
    elif not isinstance(n, unary):
        raise ValueError("Expected unary value, got %s" % type(n).__name__)

if __name__ == "__main__":
    while True:
        try:
            a=input("base-1 math equation (Recommended to use the un() function to input the numbers):\n")
            if len(a)>0:
                print(eval(a))
        except Exception as e:
             print(e)
