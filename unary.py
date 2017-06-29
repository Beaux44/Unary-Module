"""
Creates Unary integer support, includes math, addition, subtraction, multiplication, division, exponents, roots, and logarithms
"""
from math import log

def un(n):
    """Returns unary version of base-10 integer"""
    if isinstance(n, int):
        return "0"*n
    else:
        raise UnaryError("Expected type integer, got type %s" % type(n))

def unSum(n, *args):
    """Returns unary sum of any number of given unary strings"""
    a=0
    for i in args:
        a+=len(i)
    return a+len(n)

def unSub(n1, n2):
    """Returns unary absolute value of the difference between two given unary strings"""
    return un(abs(len(n1)-len(n2)))

def unMul(n, *args):
    """Returns unary product of any number of given unary strings"""
    a=1
    for i in args:
        a*=len(i)
    return un(a*len(n))

def unDiv(n1, n2):
    """Returns rounded unary qoutient of two given integers"""
    return un(round(len(n1)/len(n2)))
    #+("."+"0"*(int(str(len(n1)/len(n2))[str(len(n1)/len(n2)).find(".")+1:len(str(len(n1)/len(n2)))])*(10**(len(str(len(n1)/len(n2))[str(len(n1)/len(n2)).find(".")+1:len(str(len(n1)/len(n2)))])-1))) if len(n1)//len(n2)!=len(n1)/len(n2) else "")
    # idgaf, dis dah OG code rite here m8, get rekt 360noScope, wish dis wasn't useless (idk how I stood writing that)

def unExp(n, p):
    """Returns unary exponent using unExp(n, p) with n to the pth power"""
    return un(len(n)**p)

def unNthRt(n, root):
    """Returns the Nth root of unary string, formatted as unNthRt(n, root)"""
    return un(round(len(n)**(1/root)))

def unSqrt(n):
    """Returns square root of the given unary string"""
    return un(round(len(n)**.5))
def unMod(n1, n2):
    """Returns unary modulo of two given unary strings"""
    return un(len(n1)%len(n2))

def unLog(n, *args):
    """works just like python's normal log function, but works on unary strings, if given a log base, given in base-10"""
    if len(args) > 1:
        exit("unLog() takes at most 2 arguments,", len(args)+1, "given.")
    elif len(args) == 1:
        arg = args[0]
        return un(round(log(len(n), arg)))
    else:
        return un(round(log(len(n))))
def unLog10(n):
    """Works just like the normal log10 function, but on unary strings"""
    return un(log(len(n), 10))

if __name__ == "__main__":
    while True:
        try:
            a=input("base-1 math equation (Recommended to use the un() function to unput the numbers): ")
            eval(a)
        except Exception as e:
            print(e)
