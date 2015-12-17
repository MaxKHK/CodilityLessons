#a semiprime is a number which is a product of 2 primes
#(including 2 same primes)
#we have arrays P and Q, which define queries:
# set of numbers between P[x] and Q[x]
#We need to return number of semiprimes in each query
#each 1<=Q[x]<=P[x]<=N

def solution(N, P, Q):
    #ok, let's do it like that
    #get a list of all primes which are <=N
    #then construct an array of semiprimes
    #by picking prime and checking the products of all primes after it
    #(if product becomes larger N - break)
    #now getting our answer would be primitive 
    
    #map of prime numbers
    primeMap = [1] * (N+1)
    
    
    
    
    #0 and 1 - let's think they are not primes
    primeMap[0] = primeMap[1] = 0
    #counter of number
    i = 2
    
    #at most any non-prime could have a divisor of sqrt<n)
    while (i*i <= N):
        #found another prime
        if (primeMap[i] == 1):
            #all multiplies of i less than i^2 are already crossed out by other numbers
            k = i * i
            #just cross out any multiple of i
            while (k <= N):
                primeMap[k] = 0
                k += i
        i+=1
    
    
    #now just use the map to construct the list
    primesList = [i for i, x in enumerate(primeMap) if x == 1]
    
    
    #ok, let's construct the semi primes list
    #0 - not semiprime
    #1 - is semiprime
    semiPrimes = [0] * (N+1)
    
    
    #we just go over each prime in list one by one
    #and check all primes after it
    
    #iterate through each prime
    for firstPrimeIndex in range(0, len(primesList)):
        #pick second prime as equal or grater than first one
        for secondPrimeIndex in range(firstPrimeIndex, len(primesList)):
            #if product is greater than N - we don't add it and stop further checks
            if primesList[firstPrimeIndex] * primesList[secondPrimeIndex] > N:
                break
            #add semiprime to the map of semiprimes
            semiPrimes[primesList[firstPrimeIndex] * primesList[secondPrimeIndex]] = 1
    
    
    #now to save time on summing the array of semiprimes 
    #we may need to do it tons of times and each summing is linear in time)
    #we build a prefix sums by going from left to right and add prior element
    #to current
    for i in range(1, len(semiPrimes)):
        semiPrimes[i] += semiPrimes[i-1]
        
        
    #finally let's construct the result array
    #number of semiprimes within range i,j is 
    #difference between prefix sums in this positions
    
    #result list
    result = [0]*len(P)
    
    for i in range(0, len(P)):
    #notice the end index!
        result[i] = semiPrimes[Q[i]] - semiPrimes[P[i]-1]
    
        
    return result
