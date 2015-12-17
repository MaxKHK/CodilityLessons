#we are given 2 arrays A and B, numbered from 0 to N − 1.
#A[i] and B[i] give begin and end of element (its position on line).
#Arrays are sorted by end (ends of elements).
#Twoelements are non-overlapping if they have no common point.
#For example element [1,4] and [5,6] are not overlapping.
#We need to find maximum number of non-overlapping elements we can get
#From these 2 arrays.


#well, we are going to use greedy approach, optimizing locally.
#Locally optimal decision is to include first element
#Than we scan the array from beginning to end and include first element
#Which has the beginning after the end of the previously included element.
#Repeat untill you reach end of the array and return the number of elements you included.
#That simple!

#Why it works? The full proof is long and is located here:
#http://codesays.com/2015/solution-to-max-nonoverlapping-segments-by-codility/
#For us it is not interesting - greedy approach often works nice and gives us some proper solution so we just use it.

def solution(A, B):
    
    #Let's deal with special case first
    #empty arrays, so we have no elements to pick up
    if len(A)<1:
        return 0
    
    #Now back to the real cases of non-empty arrays
    #counter for the number of elements we included    
    #We include first element anyway
    result  = 1
    
    #end of the last element we included.
    #initially we include first element so its end becomes lastEnd
    lastEnd = B[0]
    
    #now we go over each element starting the second one (first one we have already analyzed in prior step)
    for curIndex in range(1,len(A)):
        #if start of current element is after the end of last
        #element we have included - add it to the set and
        #record that its end is now the end of last included element.\
        #Else - move on to next element
        if A[curIndex] > lastEnd:
            #we included one more element, increase the counter
            #of included elements
            result+=1
            #record that the end of  last included element is now the end of current element
            lastEnd = B[curIndex]
    
    #fine, we checked whole array, included as many elements as we could.
    #Return the result
    return result
