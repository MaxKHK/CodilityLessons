#assume x<=q - integers
#and A is an array
#slice is any A from Q to Z
#we need to return the maximum possible sum of
#slice

def solution(A):
    #ok, there is such stuff as Kadane's algorithm
    #it just goes over array and for each position calculates the maximum subarray ending
    #at that position
    #it is either element itself or one more element than the
    #maximum subaray in prev position
    #we will run kadane's algo to get maximum sum
    
    
    #max_so_far - for our result. Set it to first element since we might need to return a negative array
    max_ending_here = max_so_far = A[0]
    
    #forward pass - Kadane's algo. For case when we can have negative results
    for i in range(1,len(A)):
        max_ending_here = max(A[i], A[i] + max_ending_here)
        max_so_far = max(max_so_far, max_ending_here)
    
    
    return max_so_far
