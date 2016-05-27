# a ^ b = a * a * ... * a, b a's in total
def calculateExponent(a, b) :
    if 0 == b :
        return 1
    else :
        return a * calculateExponent(a, b - 1)

## test
a = 2
b = 3
print (a, b), ':', calculateExponent(a, b)