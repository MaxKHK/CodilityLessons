#leader - the element with freq > n/2
#equi-leader - index of the array such that leader to the left = leader to the right
#function returns the number of equileaders

def solution(A):
    #lets do it like that. Have 2 dictionaries of lists
    #each one for separate part of array
    #store in it the number of occurrences of each number so far
    #shift to right, check the leader, compare
    
    
    #our result!
    result = 0
    
    #special cases of empty or 1-element list
    if len(A) == 1:
        return result
    
    #dictionaries for left and right subarrays
    leftSide = {}
    rightSide = {}
    
    #length of each subarray
    leftLength = 1
    rightLength = len(A) - 1
    
    #initially left subarray covers first element
    #right one - rest of array
    leftSide[A[0]]=1
    
    #current leader of left
    leftSideLeader = A[0]
    leftSideLeaderCount = 1
    
    #and the right
    rightSideLeader = A[1]
    rightSideLeaderCount = 1
    rightSide[A[1]] = 1
    
    
    #populate right subarray with counts of each number
    #also find the current leader of right side
    for i in range(2,len(A)):
        if A[i] in rightSide:
            rightSide[A[i]] += 1
            #check if a right side leader now changes
            if A[i] != rightSideLeader and rightSide[A[i]] > rightSideLeaderCount:
                rightSideLeaderCount = rightSide[A[i]]
                rightSideLeader = A[i]
            elif A[i] == rightSideLeader:
                rightSideLeaderCount+=1
        else:
            rightSide[A[i]] = 1
    
    
    #lets check if we already have the equileader
    if leftSideLeader == rightSideLeader and rightSideLeaderCount > rightLength//2:
        result+=1
    
    
    #now we will shift the boundary one element at a time 
    #(add count to left side\remove count from right side)
    #and look for leaders
    for i in range(1,len(A)):
        
        #basic stuff - add\remove counts
        if A[i] not in leftSide:
            leftSide[A[i]] = 1
        else:
            leftSide[A[i]] += 1
        
        #notice that we can't face anything not already in right side
        rightSide[A[i]] -= 1
        
        #change length of sides
        leftLength+=1
        rightLength-=1
        
        #leader counts and check if leader is changed
        if A[i] == leftSideLeader:
            leftSideLeaderCount+=1
        else:
            if leftSideLeaderCount < leftSide[A[i]]:
                leftSideLeader = A[i]
                leftSideLeaderCount = leftSide[A[i]]
        
        #leader counts and check if leader is changed
        if A[i] == rightSideLeader:
            rightSideLeaderCount-=1
            if rightSideLeaderCount < rightSide[A[i]]:
                rightSideLeader = A[i]
                rightSideLeaderCount = rightSide[A[i]]
                
        
        #finally lets check if leaders are same AND REAL
        if leftSideLeader == rightSideLeader and leftSideLeaderCount > leftLength//2 and rightSideLeaderCount > rightLength//2:
            result+=1

    
    return result
