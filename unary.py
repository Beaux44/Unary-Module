"""
Creates Unary integer support, includes math, addition, subtraction, multiplication, division, exponents, roots, and logarithms
"""
from math import log

class UnaryError(Exception):
    """Error for when something impossible in unary occurs, may or may not be added upon"""
    pass


class unary:
    """My attempt at making unary numbers work more like regular base-10 integers"""
    def __init__(self, integer):
        if isinstance(integer, str):
            pass
        else:
            raise TypeError("Expected type string, got %s" % type(integer))
        self.value = len(integer)
        self.integer = integer
        if self.integer[0] == "-":
            self.value -= self.value*2
            self.integer = self.integer[1:]
        for i in str(self.integer):
            if i!="0":
                raise UnaryError("Unary has only 1 symbol")
    def __str__(self):
        return ("-" if self.value<0 else "") + str(self.integer)
    def __repr__(self):
        return "unary(\"{}\")".format(str(self), str(self.value))
    def __int__(self):
        return self.value
    def __add__(self, other):
        x = int(self) + int(other)
        return unary(("-" if x<0 else "") + "0"*abs(x))
    def __sub__(self, other):
        x = int(self) - int(other)
        return unary(("-" if x<0 else "") + "0"*abs(x))
    def __mul__(self, other):
        x = int(self) - int(other)
        return unary(("-" if x<0 else "") + "0"*abs(x))
    def __pow__(self, other):
        x = int(self)**(other if isinstance(other,float) else int(other))
        return unary(("-" if x<0 else "") + "0"*abs(x))
    def __mod__(self, other):
        x = int(self)%int(other)
        return unary(("-" if x<0 else "") + "0"*abs(x))
    def __floordiv__(self, other):
        x = int(self)//int(other)
        return unary(("-" if x<0 else "") + "0"*abs(x))
    def __truediv__(self, other):
        x = round(int(self)/int(other))
        return unary(("-" if x<0 else "") + "0"*abs(x))


def un(n):
    """Returns unary version of base-10 integer"""
    if isinstance(n, int):
        return unary(("-" if n<0 else "") + "0"*abs(n))
    else:
        raise UnaryError("Expected type integer, got type %s" % type(n))

def unSum(n, *args):
    """Returns unary sum of any number of given unary strings"""
    for i in args:
        if isinstance(i, unary):
            n+=i
        else:
            raise ValueError("Expected unary value, got %s" % type(i))
    return n

def unSub(n1, n2):
    """Returns unary absolute value of the difference between two given unary strings"""
    return un(abs(n1-n2))

def unMul(n, *args):
    """Returns unary product of any number of given unary strings"""
    for i in args:
        n*=i
    return un(a)

def unDiv(n1, n2):
    """Returns rounded unary qoutient of two given integers"""
    return un(round(n1/n2))
    #+("."+"0"*(int(str(len(n1)/len(n2))[str(len(n1)/len(n2)).find(".")+1:len(str(len(n1)/len(n2)))])*(10**(len(str(len(n1)/len(n2))[str(len(n1)/len(n2)).find(".")+1:len(str(len(n1)/len(n2)))])-1))) if len(n1)//len(n2)!=len(n1)/len(n2) else "")
    # idgaf, dis dah OG code rite here m8, get rekt 360noScope, I wish dis wasn't useless (idk how I stood writing that (the code and that sentence, for clarification))

def unExp(n, p):
    """Returns unary exponent using unExp(n, p) with n to the pth power"""
    return un(n.value**p)

def unNthRt(n, root):
    """Returns the Nth root of unary string"""
    return un(round(n**(1/root)))

def unSqrt(n):
    """Returns square root of the given unary string"""
    return un(round(n**.5))
def unMod(n1, n2):
    """Returns unary modulo of two given unary strings"""
    return un(n1%n2)

def unLog(n, *args):
    """works just like python's normal log function, but works on unary strings, if given a log base, given in base-10"""
    if len(args) > 1:
        raise TypeError("unLog() takes at most 2 arguments,", len(args)+1, "given.")
    elif len(args) == 1:
        arg = args[0]
        return un(round(log(n.value, arg)))
    else:
        return un(round(log(n.value)))
def unLog10(n):
    """Works just like the normal log10 function, but on unary strings"""
    return un(round(log(n.value, 10)))

if __name__ == "__main__":
    while True:
        # try:
            a=input("base-1 math equation (Recommended to use the un() function to input the numbers):\n")
            if len(a)>0:
                print(eval(a))
        # except Exception as e:
            # print(e)
