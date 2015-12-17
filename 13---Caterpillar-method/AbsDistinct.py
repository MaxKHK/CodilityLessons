#we are given a list A which stores elements in non-decreasing order
#our task is to count the amount of different ABSOLUTE values
#in the list. For example list -1, 0, 1, 2 contains 3 different absolute values.


#We could have done it one line (make new list with absolute values,
#convert to set and count length) but we need to practice the caterpillar method.
#So we exploit the fact that the array is ordered in non-decreasing order,
#and do it by making the head of our caterpillar at the beginning of the list
#and its tail at the end of the list. Then we shrink the caterpillar from head and 
#tail until head and tail elements match and count number of distinct elements we
#saw. Notice that we are going from elements with largest abs value to
#elements with smallest abs value (which will be located close to middle of list)


def solution(A):
    #well, there is at least one element for sure.
    #and we put into our counter for results
    result = 1
    
    #we assume that current element with which we work
    #is the one with greater absolute value of leading and tailing
    curValue = max(abs(A[0]), abs(A[-1]))
    
    #assume that head is at first element
    #and tail is at last one initially
    headIndex = 0
    tailIndex = len(A) - 1
    
    #now we repeat internal loop until head and tail merge
    #meaning until we fully shrink our caterpillar
    while headIndex <= tailIndex:
        #ok, let's record where our head is looking now
        prevHeadValue = abs(A[headIndex])
        
        #if the head and the previous element with 
        #smallest abs are same we need to skip the heading elements        
        if prevHeadValue == curValue:
            headIndex += 1
            continue
            
        
        #ok, now let's take a look at where our tail is looking now
        prevTailValue = abs(A[tailIndex])
        
        #and if our tail is looking into a value with same abs
        #as smallest abs we saw so far - we need to skip tailing elements
        if prevTailValue == curValue:
            tailIndex -= 1
            continue
            
        #finally we skipped all the stuff we wanted. Now both the head and tail
        #are looking into elements which have the different abs values from the one in
        #curValue. Let's check which one has larger abs value - tail or head
        #and make it new curValue
        
        if prevHeadValue >= prevTailValue:
            curValue = prevHeadValue
            headIndex += 1
        else:
            curValue = prevTailValue
            tailIndex -= 1
        
        #well, we met a new abs value so let's add it to counter
        
        result += 1
        
        
        
        
    #that's it, return the result
    return result
    
