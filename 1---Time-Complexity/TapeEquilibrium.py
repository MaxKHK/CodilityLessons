#we have an array and we want to split it into two parts
#such that the difference between sum of elements in each of
#2 parts is minimal. We must compute the minimal possible difference


#simple - start with first element in left part and all rest
#elements in right part. Compute the sum of right part. Then sequentially
#go throw all array and add each element to sum of all elements in left part
#and subtract it from sum in right part. And just record the minimal difference
#we encountered so far.

def solution(A):
    #initially in left part we have only first element
    sumLeft = A[0]
    #initially in right part part we have all other elements
    sumRight = sum(A[1:])
    
    #counter for minimal difference between left and right parts
    #we encountered so far.
    minDiff = abs(sumLeft - sumRight)
    
    #go through whole array (starting with second element)
    for i in range(1,len(A)-1):
        #add the current element to left sum and subtract from right sum
        sumLeft += A[i]
        sumRight -= A[i]
        #check if now we have a difference smaller than we saw before
        if abs(sumLeft - sumRight) < minDiff:
            minDiff = abs(sumLeft - sumRight)
    return minDiff
