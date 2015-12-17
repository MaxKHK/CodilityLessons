#we have a frog which initially stands at -1.
#It needs to get to other side of river (len(A)).
#It can make a jump to a leaf with a len of any fibo number.
#Array A holds 1 if there is a leaf and 0 - if no.
#We need to return a number which will show least number of jumps frog must do
#in order to get to other shore and -1 if not possibleS



#Ok, we do some dynamic programming.
#First of all we will build an array of fibo 
#numbers which are <= len(A).
#After that we go over each idx in original array and if there is a 
#leaf in that position. Than just keep increasing the jump size to see
#from which leaf closest to the beginning you could optimaly get

def solution(A):
    #let's assume that our last position is a shore
    #to maike algo slightly simpler
    A.append(1)
    #we need tfibo numbers less than that one
    N = len(A)
    
    #our fib numbers array
    fibNumbers = [0,1]
    #generate fibonacci numbers
    while fibNumbers[-1]<=N:
        fibNumbers.append(fibNumbers[-1] + fibNumbers[-2])
    
    #last element will be bigger than N, remove it
    del(fibNumbers[-1])
    
    #also drop first element (it is 0 - and we can't jump on length of 0)
    del(fibNumbers[0])
    
    #ok, fine, we have our map of possible jumps. Now let's
    #build a map of reachability - which position
    #in how many jumps we can get
    #-1 means not reachable, else we have number of jumps needed
    reachabilityMap = [-1] * N
    
    #ok, we make a first jump from a shore so lets map the leafs we can reach during first jump
    #and put 1 there - which means we get there in 1 jump
    for jump in fibNumbers:
        if A[jump-1] == 1:
            reachabilityMap[jump-1] = 1
            
    #now go over each leaf in the A array
    for i in range(0,len(A)):
        #we ignore positions where we have no leaf
        #and already discovered path
        if A[i] == 0 or reachabilityMap[i] > 0:
            continue
        #the index of an optimal leaf from which to jump to current position
        minIndex = -1
        #the amount of jumps made to reach the leaf minIndex (the optimal so far)
        #by default - even longer than river itself
        minValue = N+1
        
        #now check each possible jump and see where it leads us
        for jump in fibNumbers:
            #th position from which we could have jumped to current position
            previousLeaf = i - jump
            #we are beyond the left shore - jump is too big
            if previousLeaf < 0:
                break
            #if there is a leaf in that position
            #and it can be reached in less than current best position
            #we record that this currently best option we have
            if reachabilityMap[previousLeaf] > 0 and reachabilityMap[previousLeaf] < minValue:
                minValue = reachabilityMap[previousLeaf]
                minIndex = previousLeaf
        
        #ok, we checked all the possible jumps.
        #what we have? If we found any optimal jump
        #let's record it
        if minIndex>-1:
            reachabilityMap[i] = minValue+1
            

            
    #after we checked each leaf - return the optimal value for last leaf (which we placed
    #on right shore)
    
    return reachabilityMap[-1]
