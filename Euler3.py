def LPF(n):
    m=3
    while m<n:
        if n%m==0 and checkIfPrime(n/m):
            return n/m
        else:
            m+=2
    return 1

def checkIfPrime(value):
    possibleFactor=3
    while possibleFactor<value/2:
        if value%possibleFactor==0:
            return False
        else:
            possibleFactor+=2
    return True
