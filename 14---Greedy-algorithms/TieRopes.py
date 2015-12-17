#we are given an array A. Each element represents the length
#of a rope. Ropes lie in a line one after each other. Adjustent ropes
#can be tied (under adjustent we mean rope i and i+1). Result of this action
#is a new rope with a lenggth of A[i] + A[i+1]. That new rope can be used again to
#tie it with next rope and so on.
#We are also given an integer 4. Our task is to find the way to tie
#ropes in array A in such a way so that each resulting rope is longer or equal to K
#and we have maximum number of ropes.
#For example if A = [1,2,3,4,1,1,3] and K = 4 we can tie:
# - rope 1 with rope 2 to produce a rope of length A[1] + A[2] = 5;
# - rope 4 with rope 5 with rope 6 to produce a rope of length A[4] + A[5] + A[6] = 5.
#After that, there will be three ropes whose lengths are greater than or equal to K = 4. It is not possible to produce four such ropes.


#well, we are using greedy approach and just go over the array from start to end.
#We pick up first rope and keep tying subsequent ropes to it untill we get a length >= K. Then
#We increase the counter and pick up next rope, repeating this same action untill the array finishes.
#Approach is extremely naive but, well, it is a greedy algorithm section and it works fine


def solution(K, A):
    #counter for result
    result = 0
    
    #counter for length of the rope we are currently holding
    curLength = 0
    
    #pick up each rope, from start to end of array
    for rope in A:
        #tie the rope we picked up with the rope we already building
        curLength += rope
        
        #if the result of tie is a rope longer than K
        #we drop this new rope and move on the new one
        if curLength >= K:
            result+=1
            curLength = 0
    
    #that's it, return the result
    return result
