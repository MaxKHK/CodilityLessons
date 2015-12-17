#we get the Array. We should divide the array A into K
#blocks such that we minimize the maximum sum of elements
#in blocks (blocks can be empty).
#notice - ignore M, it is not the Maximum element in A


#Ok, we do a binary search using the maximum sum as a 
#function which we minimize
#We define range as that minimum sum is the maximum element
#and that the maximum sum is the sum of whole array
#Than we jus do a classical binary search, splitting the range and checking the median element
#with a function which will check if we can achieve such a sum in K blocks



#function which checks if we can achieve the division of array into 
#specified number of blocks such that we have a target maximum sum 
def checkTheHypothesis(Array, TargetSum, NumOfBlocksAllowed):
    #ok, we do the check in really simple way
    #we assume that sum of block is 0 initially and
    #sequentially add next array elements to it, tracking current sum. Once the sum becomes
    #larger than target sum - we start new block and repeat the process
    #If we find out that we need more blocks than we are allowed to have
    #we break and kill the process - we can't achieve the TargetSum
    #if we get to the end of array successfully - than the division is possible
    
    #ok, we start with a 0 sum initially
    currentBlockSum = 0
    currentNumOfBlocks = 1
    
    
    #we go over each element in array
    for element in Array:
        #check if the sum of current block will be larger 
        #if we add the current element to it
        if currentBlockSum + element > TargetSum:
            #it becomes larger, we reset and start over the new block
            currentBlockSum = element
            currentNumOfBlocks+=1
            #is it possible for us to start another block
            #or we are not allowed to have that many blocks?
            if currentNumOfBlocks>NumOfBlocksAllowed:
                #we need more blocks to achieve the target sum, so the division is not possible
                return False
        else:
            #it won't become larger, so we just add an element to array
            currentBlockSum+=element
    
    #if we successfully went through the array - we can achieve the required division
    return True

#function which will actually perform the binary search
def doBinarySearch(Array, NumOfBlocksAllowed, ArrayLen):
    
    
    #lower bound is a biggest element (obviously it will be in some block)
    lowerBound = max(Array)
    #we can't get larger block sum than sum of whole array
    higherBound = sum(Array)   
    
    #now we perform binary search and narrow the gap
    #between lower and higher bounds untill they merge
    #after that we return the lower bound
    while lowerBound <= higherBound:
        #our candidate is in the middle of current range
        candidateSum = (lowerBound + higherBound)/2
        #let's check this candidate
        if checkTheHypothesis(Array, candidateSum, NumOfBlocksAllowed):
            #we can achieve the division - so let's try something smaller
            higherBound = candidateSum - 1
        else:
            #we can't achieve such division in K blocks - try something larger
            lowerBound = candidateSum + 1
            
    return lowerBound
            
#it just runs the binary search    
def solution(K, M, A):
    #we need a len of array
    N = len(A)
    
    #couple of special cases - we can get their results instantly
    if K>=N:
        return max(A)
    if K==1:
        return sum(A)
        
    #run the binary search and return its result
    return doBinarySearch(A, K, N)
