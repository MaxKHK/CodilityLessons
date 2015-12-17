#we are given a list of N integers
#each integer is within range 1...N
#for each integer i in array
#we want to check how many other integers in that array
#are non divisors of i
#we need a function which will return a sequence of
#such numbers

def solution(A):
    #Build a map of divisors for each number less than
    #biggest number using the Sieve of Eratosthenes.
    #After that go over each element in original array
    #and count its number of occurrences
    #Finally go over each element in original array
    #and set the result as length of array minus 
    #number of occurrences of each of its divisors
    
    
    #some basic variables
    N = len(A)
    MaxA = max(A)
    
    #dictionary which will store divisors of each number
    #we are interested in
    divisorMap = {}
    
    
    #each number has a divisor of 1
    for element in A:
        divisorMap[element] = [1]
    
    #now let's go over each possible divisor - it should be
    #less than or equal maximum element (and 1 is already in list0
    for divisor in range(2, MaxA+1):
        #we will go over each multiple of divisor 
        #starting with the one equal to divisor itself
        multiple = divisor
        while multiple <= MaxA:
            #if multiple is in map of divisors, meaning
            #it is in the original array
            #and the divisor is not in the the list of divisors yet
            #add the divisor to the list of divisors of multiple
            if multiple in divisorMap and divisor not in divisorMap[multiple]:
                divisorMap[multiple].append(divisor)
            #just increment by divisor to get new multiple
            multiple+=divisor
            
    
    #now compute the number of occurrences of each member
    #of original array
    divisorsCount = {}
    for element in A:
        divisorsCount[element] = divisorsCount.get(element,0)+1
        
        
    #construct the result array
    #just pick each element and
    #get the total amount of occurrences
    #of each of its divisors and subtract it
    #from array length to get number of items in array
    #which are not divisors of the number
    
    result = []
    
    for element in A:
        totalDivisors = sum([divisorsCount.get(divisor,0) for divisor in divisorMap[element]])
        result.append(N - totalDivisors)
    return result
