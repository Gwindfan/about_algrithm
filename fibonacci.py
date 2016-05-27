# Three key features of recursion implementation
# base case: return 1 if n == or n ==1
# recursion goes towards base case
# function calls itself

# A sequence of numbers like 0 1 1 2 3 5 ...
def calculateFibonacci(n): 
    if 1 == n :
        return 1
    elif 0 == n :
        return 0
    else :
        return calculateFibonacci(n -1) + calculateFibonacci(n - 2)
    
# test
n = 10
for i in range(n) :
    print i, calculateFibonacci(i)
    