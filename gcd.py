## greatest common divisor
def calculateGcd(a, b) :
    if 0 == b :
        return a
    else :
        return calculateGcd(b, a % b)
         
## test
a = 10
b = 20
print (a, b), ':', calculateGcd(a, b)