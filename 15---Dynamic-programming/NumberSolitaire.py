#We have an array A of N numbers. Imagine that this is a band
#With a squares and in each square we have a number written as in array A.
#We also have a peeble in position 0 initially. Position 0 is marked.
#Than we throw a dice with numbers 1-6 and move a peeble to position
#i + what we have on a dice. If the position doesn't exist we repeat the throw
#untill we get the result which is valid. When pebble settles on any position
#we mark it. Once the pebble settles on last position in a band we stop the game.
#Than we calculat ethe result of the game - it is the sum of numbers in all 
#marked positions. Our task is to write the function which for array A will calculate
#maximum possible result of the game. For example if we have array A = [1,-2,0,9,-1,-2]
#one possible game could be as follows:
#1) the pebble is on square number 0, which is marked;
#2) we throw 3; the pebble moves from square number 0 to square number 3; we mark square number 3;
#3) we throw 5; the pebble does not move, since there is no square number 8 on the board;
#4) we throw 2; the pebble moves to square number 5; we mark this square and the game ends.
# The marked squares are 0, 3 and 5, so the result of the game is 1 + 9 + (−2) = 8. 
#This is the maximal possible result that can be achieved on this board.


#We use a dynamic programming approach which is that we solve the sequence of smaller tasks
#using the solutions of previous tasks to arrive at the final solution.
#In our case we can answer the question at hand - which maximum possible sum of marked positions we could have
#after getting to last position in a simple way - it is maximum possible sum we can get by getting into any position
#from end-6 (we can get from it to end by getting 6 on dice) to end-1 (we will need 1 on dice) and add to it a value
#written in last position. We can answer the questions like 'which maximum possible sum we get by getting into position end-5'
#in exact same way.
#So we will incrementally build an array DP which will record which maximum possible sum we can get by getting
#into position DP[i]. We will pick up each element in array DP one by one and each moment we just check which of the 6 elements
#before it offer the maximum possible sum. Then we add value of element A in the same position to get maximum possible
#sum for current position. When we arrive at the last position of DP we will be able to calculate our answer.


def solution(A):
    
    #here is our array which will hold the maximum possible sums for each position
    #initially contains zeros
    DP = [0] * len(A)
    
    #initially peeble is in the first position of a band
    #and for that position maximum possible sum is obviously is the value
    #of first element itself
    DP[0] = A[0]
    
    #now lets go over each position in band
    #starting from second position (we already visited first position, peeble is already there)
    for curIdx in range(1,len(A)):
        #now, we have at most six possible previous positions from which we can get to the current position
        #since dice can show us numbers 1-6. We will check each possible previous position now
        
        #first of all we need a counter for maximum possible sum of any previous positions
        #We initially set it as smallest possible number ever - negative infinity
        maximumSum = -float("inf")
        
        
        #each possible dice value
        for dice in range (1,7):
            #let's calculate from which position we should have moved with such dice value
            #to get to current position
            priorPosition = curIdx - dice
            #well, the result should be positive,
            #there is no way to get to position 2 with a dice value of , for example
            if priorPosition >= 0:
                #ok, since it is a real case now let's test if the maximum possible sum for that position
                #is bigger than anything we saw before
                if DP[priorPosition] > maximumSum:
                    #we found a maximum sum which is better! Let's record it
                    maximumSum = DP[priorPosition]
                    
        #nice, we went over each possible dice value and now we know which maximum sum
        #we have in any previous position we can reach with a jump of a length less than 0
        #Now maximum possible sum for current element is a maximum possible sum we found plus
        #value of the element itself
        DP[curIdx] = A[curIdx] + maximumSum
    
    
    
    #that's it, we went over whole array and now last element of DP shows us maximum possible sum we can get
    #when reaching this position.
    return DP[-1]
