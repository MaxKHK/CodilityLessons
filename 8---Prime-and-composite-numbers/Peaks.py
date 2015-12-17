#a function which returns the maximum number
#of peak bocks in which array A can be divided
#a peak is like 2,3,1 or 1,2,1 or smth like it.

def solution(A):
    #ok, let's be conservative -
    #first get all the picks positions
    #second - go over each possible group size
    #and check that each of the groups formed by
    #such size have at least one pick
    
    
    #let's find all peaks
    peaks = []
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.append(i)
    
    
    #couple of special cases
    if len(peaks) == 0:
        return 0
    
    if len(peaks) == 1:
        return 1

    
            
    #now we just go over numbers less than len(N)
    #and check if it is a divisor of N. If yes - 
    #test the groups of such size
    #first time we find such a group - we are done, subsequent groups will yeild
    #smaller amount of groups
    
    positionPrev = 0
    
    
    
    for groupSize in range(1, len(A)):
        #divisible, so it is a valid group size
        if len(A) % groupSize == 0:
            #get the number of groups
            numGroups = len(A)//groupSize
            #matrix of fine\not fine groups
            groupStatus = [False] * numGroups           
            #go over each peak and use it
            for peak in peaks:
                #to get the number of block in which we fall
                #just do an int division
                blockNum = peak//groupSize
                #mark that the group is fine
                groupStatus[blockNum] = True
            
            #final check - if all groups are fine - return the result
            if False not in groupStatus:
                return numGroups
            
    #not returned anywhere before - we can't split it anyhow
    #but in a single pack
    return 1  
