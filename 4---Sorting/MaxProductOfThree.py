#returns maximum product of triplet within an array

def solution(A):
    #obvious cases - product of three largest elements in array
    #product of 2 smallest elements and a largest element
    
    #sort array
    A.sort()
    #first case - three largest
    firstProduct = A[-1]*A[-2]*A[-3]
    #second case - 2 smallest and largest one
    secondProduct = A[0]*A[1]*A[-1]
    
    #return the one which is larger
    if secondProduct > firstProduct:
        return secondProduct
    else:
        return firstProduct
