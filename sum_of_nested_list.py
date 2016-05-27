## Calculate sum of nested list
def calculateSumOfNestedList(list):
    sum = 0
    for e in list :
        if type(e) != type([]) :
            sum += e
        else :
            sum += calculateSumOfNestedList(e)
    return sum

## test
list = [1, -1, [2, -2], [3, -3, [4, -4], 10]]
print 'sum is: ', calculateSumOfNestedList(list)