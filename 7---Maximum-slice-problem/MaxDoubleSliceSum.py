#assume x<y<z - integers
#and A is an array
#double slice is any A from X to Y
#and A from Y to Z
#we need to return the maximum possible sum of
#these 2 slices
#notice - empty slices are possible with sum of 0

def solution(A):
    #ok, there is such stuff as Kadane's algorithm
    #it just goes over array and for each position calculates the maximum subarray ending
    #at that position
    #it is either 0 (empty array) or one more element than the
    #maximum subaray in prev position
    #we will run kadane's algo in forward and backward passes
    #store its results in 2 arrays
    #and then maximize the sum of double slices (to left and to righ of index)
    
    
    #arrays for forward and backward passes
    KadaneForward = [0]*len(A)
    KadaneBackward = [0]*len(A)
    
    #forward pass - Kadane's algo. Notice we may ignore first and last elements - 
    #by definition of double slice they can't be included
    for i in range(1,len(A)-1):
        KadaneForward[i] = max(0, A[i] + KadaneForward[i-1])
        
    #backward pass, much the same as prior, just go backward
    for i in range(len(A)-2, 0, -1):
        KadaneBackward[i] = max(0, A[i]+KadaneBackward[i+1])
        
        
    #now lets go and get the maximum possible double slice
    #recall that double slice is A[X+1]+..+A[Y-1]+A[Y+1]+...+A[Z-1]
    result = 0
    for i in range(1,len(A)-1):
        result = max(result,KadaneForward[i-1]+KadaneBackward[i+1])
    
    return result
