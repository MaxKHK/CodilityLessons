#returns 1 if we can built a triangle from this array
#triangle could be built if there is a triplet where
#sum of each 2 members bigger than third one

def solution(A):
    
    #we need at least 3 points
    if len(A)<3:
        return 0
    else:
        #sort it
        A.sort()
        #go over each of member
        #since array is sorted, if sum of A[i] and A[i+1] > A[i+2] 
        #2 other sums will be satisfied automatically! (sum becomes bigger,
        #third element smaller
        for i in range(0, len(A)-2):
            if A[i] + A[i+1] > A[i+2]:
                return 1
        return 0
    
