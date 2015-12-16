#function to find the slice with minimal average
#the key idea is that there MUST be a two-slice or three-slice
#which holds minimal value - since all other slices could be
#break down into two-slices or three-slices
#NOTE: there might be longer slices of SAME average, but not smaller
def solution(A):
    
    #we know that the values smaller than 10001
    minValue = 10001
    #index of minimal slice
    minIndex = 0
    
    for i in range(0, len(A)-1):
        #check two-slice
        if (A[i] + A[i+1])/2.0 < minValue:
            minValue = (A[i] + A[i+1])/2.0
            minIndex = i
        #check three-slice
        if i<len(A)-2 and (A[i] + A[i+1] + A[i+2])/3.0<minValue:
            minValue = (A[i] + A[i+1] + A[i+2])/3.0
            minIndex = i
    return minIndex
    
