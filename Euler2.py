

def fibSumOfEven():
    evenValues=[2]
    fibStoredValues={1:1,2:2}
    counter=3
    endConditionValue=4000000
    totalValue=0
    fibValue=2

    while fibValue<=endConditionValue :
        fibValue=getEvenValues(counter,evenValues,fibStoredValues)
        counter+=1

    for values in evenValues:
            totalValue+=values
    return totalValue

def getEvenValues(n,storedEvenValues,fibStoredValues):
    if n in fibStoredValues:
        return fibStoredValues[n]
    else:
        value=getEvenValues(n-1,storedEvenValues,fibStoredValues)+getEvenValues(n-2,storedEvenValues,fibStoredValues)
        fibStoredValues[n]=value
        if value%2==0:
            storedEvenValues.append(value)
        return value
