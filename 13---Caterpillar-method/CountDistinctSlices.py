#we have an integer M and a list A. Each element of A
#is <= M. A pair of integers 0<= P<=Q<=N defines a slice
#which includes members between P and Q (A[P:Q]).
#Distinct Slice is a slice which consists of only unique numbers
#We need to count number of distinct slices within an array.
#For example for array [3,4,5,5,2] There are exactly nine 
#distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).



#We use a caterpillar method. Initially we put head and tail 
#of caterpillar at the beginning of the array. Then we move
#head towards the end of an array one step at a time. On each step
#we add to result the (head - tail + 1), since this is the number of
#sub slices we can have. Why? Well, for example we have numbers 1,2,3.
#So head is 2, tail is 0. We can have subslices: [1], [1,2], [1,2,3], 
#which is 2 - 0 + 1 = 3 subslices. We do not include subslice [2,3]
#since we will cover it when tail will be located at element 2.
#Ok, also at each step we check if the element we picked up now
#and mark in predefined array of length M if we saw this element previously.
#If we encounter element we already saw - we start to push
#the tail toward the end of array until tail passes the duplicating element.
#While moving tail to the end of array we also remove each element it passes
#from an array which holds the list of seen elements.
#When head or tail get to the end of array we stop the process.
#If number of distinct slices is > 1000000000 = we return 1000000000



def solution(M,A):
    #counter for result
    numDistSlices = 0
    
    #initially head and tail are at the beginning of array
    headIndex = 0
    tailIndex = 0
    
    #array which will hold which elements we already saw\
    #We know that M is the biggest possible element
    seenNumbers = [False] * (M+1)
    
    #no we move head toward the end of array
    while (headIndex < len(A) and tailIndex < len(A)):
        #we move the head towards the end of array
        #until we encounter some element which we have already seen
        while (headIndex < len(A) and seenNumbers[A[headIndex]] == False):
            #ok, we add number of subslices between head and tail
            #to result counter (see explanation earlier)
            numDistSlices += (headIndex - tailIndex + 1)
            #if it bigger than 1000000000 we can safely stop
            #and return 1000000000
            if numDistSlices >= 1000000000:
                return 1000000000
            #now mark that we have seen current element
            seenNumbers[A[headIndex]] = True
            #and move the head further
            headIndex+=1
        #that will run when caterpillar head will point
        #at number we have already seen.
        else:
            #we move the tail until tail will get to the element at which
            #head is looking right now. This head element should be the one we have seen
            #previously so we are trying to get the tail across it.
            while (headIndex < len(A) and tailIndex < len(A) and A[headIndex] != A[tailIndex]):
                #remove the number at tail from list of the number we saw
                seenNumbers[A[tailIndex]] = False
                #move tail further
                tailIndex+=1
            #ok as we know prior cycle will stop when tail will look at same
            #element as head. So we need to move tail one step further to exclude
            #that element from caterpillar so that it has no dupes and can move on
            seenNumbers[A[tailIndex]] = False
            tailIndex += 1
            
        
    #well, let's return the results, shall we?
    return numDistSlices
