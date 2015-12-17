#dominator - the element with freq > n/2
#function returns the index of any dominator (if any)

def solution(A):
    #ok, we will do this simple - dominator remains same even if
    #we remove to different elements from array
    #remove 2 different elements each time and see what is left
    #then test if element which is left is a real dominator
    #finally, look for its index
    
    
    #special cases of empty or 1-element list
    if len(A) == 1:
        return 0
    if len(A) == 0:
        return -1
    
    
    #length of stack
    stackLength = 1
    #top of stack (notice, everything under the top of stack is still the same)
    stackValue = A[0]
    
    #last index of a potential dominator
    idxDominator = 0
    
    #go over each element
    for i in range(1, len(A)):
        #stack is empty - put value on top
        if stackLength == 0:
            stackValue = A[i]
            idxDominator = i
            stackLength+=1
        #same as current top o stack - just increase the length
        if stackValue == A[i]:
            stackLength+=1
            idxDominator = i
        #pair of different elements - delete it, decrease the length
        else:
            stackLength-=1
    
    #ok, if we don't have anything left in stack after iterations - 
    #there is no dominator
    if stackLength == 0:
        return -1
        
    #our value left in stack is our candidate for being a dominator. Test it for frequency
    if A.count(stackValue) > (len(A)//2):
        #a dominator!
        return idxDominator
    else:
        return -1
