#we get the arrays A and B. They represent start of plank (array A)
#and end of plank (array B). We also get an array C which shows
#positions of nails. Our task is to find, how many of first X nails from C
#we must use to nail all the planks (plank is nailed if Start<= Nail <= End)



#Ok, we do a binary search trying to minimize the number of first
#nails from C array. We pick up some number of first X nails from C
#and check if it can nail all of the planks. Before doing this we sort the positions of all nails
#we check this time (and also we sort the planks by their start).
#We are checking if we can nail all of the planks by picking up nail
#and then incrementally go over each plank and check if it satisfies
#the condition start<=nail<=end. When the plank Start is beyond the current nail
#we go to the next nail. If after we picked up all nails we have picked all planks - 
#we had enough nails to nail all planks.



#function which checks if we can nail all the planks
#with the nails we were given.
def checkTheHypothesis(ArrayPlanks, ArrayNails):
    #this is the tricky part.
    #we go over each nail in an array. We remove planks until
    #their start overshoots the nail - in such case we pick next nail.
    #If some plank remains unnailed - we break the algorithm!
    #Finally we check if nailed all the planks
    
    #Our planks are sorted by start, but we need to sort the nails first
    #since they are not in the sorted order in original array
    ArrayNails = sorted(ArrayNails)
    
    #counter of how many planks we need to nail (notice that len() function is O(1)
    #so you don't need to precalc it once and path to current function)
    PlanksToNail = len(ArrayPlanks)
    
    #counters of current nail and current plank
    #we are checking
    
    currentNail = 0
    currentPlank = 0
    
    #total number of nails we are checking this time
    numOfNails = len(ArrayNails)
    
    #we loop until we get all the planks nailed
    while PlanksToNail>0:
        #first of all - have we ran out of nails?
        if currentNail == numOfNails:
            break
        #check if current plank can be nailed with current nail
        #at least in theory (its Start is before the nail)
        if ArrayPlanks[currentPlank][0] <= ArrayNails[currentNail]:
            #now there are 2 options here - we really can nail it (end is after the nail)
            if ArrayPlanks[currentPlank][1] >= ArrayNails[currentNail]:
                #we can nail it - remove it from queue
                PlanksToNail-=1
                currentPlank+=1
            #we can't nail it - end is before the nail.
            #And since both nails and planks are ordered - we can't nail it ever
            else:
                return False
        #ok, we need to use next nail
        else:
            currentNail+=1
    
    #ok, have we nailed everything?
    if PlanksToNail == 0:
        return True
    else:
        return False

#function which will actually perform the binary search
def doBinarySearch(ArrayPlanks, ArrayNails):
    
    #lower bound is 1 (well, we can't use less than 1 nail)
    lowerBound = 1
    #upper bound is all nails we have
    higherBound = len(ArrayNails)
    
    #now we perform binary search and narrow the gap
    #between lower and higher bounds until they merge
    #after that we return the lower bound
    while lowerBound <= higherBound:
        #our candidate is in the middle of current range
        candidateNails = int((lowerBound + higherBound)/2)
        #let's check this candidate
        if checkTheHypothesis(ArrayPlanks, ArrayNails[:candidateNails]):
            #we can nail all the stuff - so let's try something smaller
            higherBound = candidateNails - 1
        else:
            #we can't nail all the stuff - try something larger
            lowerBound = candidateNails + 1
    
    #now, it is possible that we are not able to nail all the planks - in such case
    #we would search till the maximum of the array. We need to check if it is the case
    #notice we use +1 since we used <= in while loop
    if lowerBound == higherBound+1 and not checkTheHypothesis(ArrayPlanks, ArrayNails):
        return -1
    
    #well, return the result
    return lowerBound
            
#it just runs the binary search    
def solution(A, B, C):
    #we first merge the A and B arrays into single array
    #which will have both start and end of plank in each
    #element and will have the planks sorted by their start
    
    #just join 2 lists
    ArrayPlanks = list(zip(A,B))
    
    from operator import itemgetter
    
    #and sort them by start (we use itemgetter for faster implementation)
    ArrayPlanks = sorted(ArrayPlanks, key=itemgetter(1))
    
    
    #run the binary search and return its result
    return doBinarySearch(ArrayPlanks, C)
