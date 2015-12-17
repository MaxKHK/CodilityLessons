#We are given an array A with N integers.
#The abs sum of two is the abs value of sum of two elements
#in array. We need to find minimal abs sum of two within an array.
#For example for array A = [1,4,-3] the minimal abs sum of two will be for
#|4 + (-3)| = 1. And the function should return 1 n such case.


#Ok, we apply a following algorithm.
#0). Sort the array in increasing order
#1) Check special cases:
#   1.a.) If First element of sorted array >=0 - 
#         all members of array are >= 0, and min abs sum of two
#         will be A[0] + A[0]
#   1.b) If Last element of sorted array <= 0 - 
#         all members of array are <= 0, and min abs sum of two
#         will be A[-1] + A[-1]
#2) Now, obviously we would have a mix a positive and negative integers in array
#So we are using the caterpillar method. We put the tail at the beginning of array and head
#at the end of array. hen we start to shrink the caterpillar one step at a time:
#   2.a) Check if the current abs(A[tail] + A[head]) is the smallest abs sum of two. If yes - record this fact.
#   2.b) If abs(A[tail+1] + A[head]) <= abs(A[tail] + A[head]) - move tail to this new more optimal position
#   2.c) If abs(A[tail] + A[head-1]) <= abs(A[tail] + A[head]) - move head to this new more optimal position
#   2.d) If none of the above was true - move head to head-1 and tail to tail+1
#We repeat all this stuff until head and tail met somewhere in the middle of the array.
#As a result of that we should have found a smallest abs sum of two possible. The proof is below.
#Assume that X and Y are positions for 2 elements with minimal abs sum of two. We know that array is sorted.
#Assume that we first touched the X (put a tail into it). In such case we need to ensure that as a result of algorithm
#Our head will move to position Y finally. There are 2 options here. 
#1) If A[X] + A[Y] >=0: the array is sorted , so for all i > Y, we have
#A[X] + A[i] >= A[X] + A[i-1] >= 0.
#=> A[X] + A[-1] >= A[X] + A[-2] >= ... >= A[X] + A[Y+1] >= A[X] + A[Y] >=0
#=> |A[X] + A[-1]| >= |A[X] + A[-2]| >=... >= |A[X] + A[Y+1]| >= |A[X] + A[Y]| >=0.
#So our algorithm will guide us to move from any position after Y to Y finally.
#To sum up - if currenty tail is at the X and head is AFTER Y each move of head
#towards the tail will make it closer to Y and finally we touch Y.
#2) If A[X] + A[Y] < 0: let a = |A[X] + A[Y]|, A[X] + A[Y+1] >= A[X] + A[Y] = -a with sorted array:
#If A[X] + A[Y+1] == -a or a, switch to prove with answer positions (X, Y+1);
#If A[X] + A[Y+1] is in range (-a, a), then |A[X] + A[Y+1]| < a = |A[X] + A[Y]|. It is contradict with the assumption |A[X] + A[Y]| is the minimal. Thus this case is not possible.
#If A[X] + A[Y+1] > a > 0, prove with the steps in 1
#So to sum up it is not possible for us to ever MISS the Y element as a result of our agorithm.
#You can apply same proof for case we first touch Y - proof is same, just replace X with Y :)

#Ok, with that out of the way, here is an implementation.

def solution(A):
    #We sort the array in non-decreasing order
    A.sort()
    #Now let's put out of the way couple of special cases
    
    #If First element of sorted array >=0 - 
    #all members of array are >= 0, and min abs sum of two
    #will be A[0] + A[0]
    if A[0] >= 0:
        return A[0] + A[0]
        
    #If Last element of sorted array <= 0 - 
    #all members of array are <= 0, and min abs sum of two
    #will be A[-1] + A[-1]
    if A[-1]<=0:
        return abs(A[-1] + A[-1])
    
    #With them out of the way, let's build our caterpillar.
    #Here we store our head and tail of the array
    #Initially tail is at beginning of array
    #And head at the end of the array
    head = len(A)-1
    tail = 0
    
    #here is the counter for result. Initially set it to sum of 2 largest numbers in array
    #since array is sorted
    minAbsSumOfTwo = abs(A[-1] + A[-1])
    
    #now we will shrink our caterpillar until head and tail meet
    # somewhere in the middle of the array
    
    while tail<=head:
        #let's check what is abs sum of two of current
        #head and tail
        currentAbsSumOfTwo = abs(A[head] + A[tail])
        
        #now we check if it is less than any abs sum of two we seen so far
        #and record it if needed
        if currentAbsSumOfTwo < minAbsSumOfTwo:
            minAbsSumOfTwo = currentAbsSumOfTwo
        
        #now we either move head or tail to new position
        #based on which option would be better.
        #Or if both options are not good - move both head and tail
        if abs(A[tail+1] + A[head]) <= currentAbsSumOfTwo:
            tail += 1
        elif abs(A[tail] + A[head-1]) <= currentAbsSumOfTwo:
            head -= 1
        else:
            head -= 1
            tail += 1

    #after the prior loop has completed - return the results
    return minAbsSumOfTwo
