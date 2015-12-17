#assume an array of stock prices
#find the maximum possible profit of 
#single stock trade

def solution(A):
    #let's just go throught an array
    #and calculate maximum possible profit for each position
    #by keeping track of lowest value we saw so far
    #and checking the profit for current index
    #if less than 0 - record as 0
    
    #array for profits
    ProfitsPossible = [0]*len(A)
    
    #for our result
    result = 0
    
    #empty array - no profit
    if len(A) <= 1:
        return result
    
    
    #variable for lowest price we encountered so far
    lowestPrice = A[0]
    
    
    #go over array (don't need to consider first element - it is in lowestPrice)
    for i in range(1,len(A)):
        lowestPrice = min(lowestPrice,A[i])
        ProfitsPossible[i] = max(0, A[i] - lowestPrice)
    
    
    #now just find largest possible value
    result = max(ProfitsPossible)
    
    return result
