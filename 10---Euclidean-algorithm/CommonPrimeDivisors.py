#A prime divisor of N is a prime number which divides A
#We have 2 arrays - A and B, both hold numbers.
#We want a function which will check each pair of numbers in these
#Arrays and see if prime divisors are same for that 2 numbers
#And count number of occurrences of such pairs

#SEE FULL SOLUTION DESCRITPTION IN def solution(A,B) part


#gcd function implementation
def gcd(x, y):
    if x%y == 0:
        return y;
    else:
        return gcd(y, x%y)

#function which checks if 2 integers have
#same prime divisors
def isSamePrimeDiv(x, y):
    #our gcd between x and y, which contains
    #all of their common prime divisors
    gcdOriginal = gcd(x, y)
    
    #now let's try to decompose our x into
    #common divisors in gcd by sequentially dividing it
    #until we get x == 1
    while x!=1:
        #ok, we check the gcd between original gcd and what remains of x
        xGcd = gcd(x, gcdOriginal)
        #well, we ran out of common prime divisors
        if xGcd == 1:
            break
        #divide x by that new gcd to remove some of prime divisor powers
        x /= xGcd
    
    
    #assuming that x and y have same prime divisors
    #that are in gcdOriginal, x should compose only of different powers of
    #there gcds. Thus after previous loop x should have boiled down to 1
    #which means it is not divided by any prime not in gcdOriginal
    if x!= 1:
        return False
    
    
    #let's perform same procedure for y:
    while y!=1:
        yGcd = gcd(y, gcdOriginal)
        if yGcd == 1:
            break
        y /= yGcd
        
    return y == 1


def solution(A, B):
    #Let's use fancy idea - gcd of 2 numbers
    #contains all of their common prime divisors (you could prove it yourself).
    #Thus, for each pair of numbers we first find their gcd and then
    #we: 1) Sequentally find gcd for x and original gcd. Then we divide x by that new
    #gcd and return to loop - we just try to dismantle the x into all of members
    #of gcd. 2) do the same for y. If we succeed - they have same prime divisors
    #finally we  just run that function against each pair
    count=0
    for x,y in zip(A,B):
        if isSamePrimeDiv(x,y):
            count+=1
            
    return count
