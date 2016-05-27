# n! = n * (n - 1) * (n -2) * ... * 1
def calculateFactorial(n) :
    if 1 == n :
        return 1
    else :
        return n * calculateFactorial(n - 1)
    
    
## test
n = 5
print n, calculateFactorial(n)
    