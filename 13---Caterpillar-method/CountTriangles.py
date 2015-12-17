#we are given a list A of N integers. A triplet
#0<P<Q<R<N is a triangle if we can construct a triangle out of it
#i.e. A[P] + A[Q] > A[R] and A[Q] + A[R] > A[P] and A[R] + A[P] > A[Q]
#We need to write a function which will count number of triangles
#which we can construct from array A


#Ok, honestly it is a copy of a task from reading material for this module,
#Except the fact that list here is not sorted. But sorting is done in O(N*log(N)) time
#while the algorithm we are going to use will O(N^2) so the algo will dominate
#sorting and we just sort the initial array and then apply the same algorithm as in
#reading material. Which is, for sorted array A we go from left to right picking one element
#at a time and treating it as tail of caterpillar. Than we start to move the middle of caterpillar
#from position tail+1 towards the end of array. Finally inside that loop we are moving the head
#of a caterpillar towards the end of array from position middle+1 one step at a time
#while it is true that A[tail] + A[middle] > A[head]. Notice that we can include
#each element which has A[head] < than the one which violates the condition above.
#The number of triangles for defined configuration after the inner loop for head
#is completed is defined by head - middle - 1. For example we have tail in position 0
#middle in position 1 and we were able to move head until position 4 when it violated the condition 
#for A[tail] + A[middle] > A[head]. This is our array, to illustrate: A = [5,7,9,10,13,18]. A[Tail] = 5,
#A[middle] = 7, for position 5 A[head] = 13, when we exit the loop. How many triangles we found ?
#they are [5,7,9], [5,7,10] which is head - middle - 1 or 4 - 1 - 1 = 2.


def solution(A):
    #let's measure the len of array
    n = len(A)
    
    #counter for result is here
    numTriangles = 0
    
    #now let's sort the array so that the algorithm works
    A.sort()
    
    #ok, let's put tail in the first element of array
    #and go over each possible tail (we use n-2 since we need to allow 2
    #points after the tail!)
    for tail in range(0, n - 2):
        #now, for each tail we put middle in the position right after the
        #tail. And also we initially put for each tail a head into the position
        #the point after middle. Now we check each possible middle
        #We use n-1 since we need to allow for head after the middle
        head = tail + 2
        for middle in range(tail+1, n-1):
            #now let's check each possible head - we move the head to the right
            #until it violates the condition
            while head < n and A[tail] + A[middle] > A[head]:
                head += 1
            #now let's get the amount of triangles we have found
            numTriangles += head - middle - 1

    #well, that' it, return the numTriangles
    return numTriangles
