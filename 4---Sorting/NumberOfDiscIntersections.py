#function calcs the number of intersected discs
#A[J] disc is drawn from J point with radius of A[J]
#intersection is if J!=K and they have point in common (at least point)


def solution(A):
    #construct a lists of start and end points
    pointsStart = []
    pointsEnd = []
    for i in range(0,len(A)):
        pointsStart.append(i-A[i])
        pointsEnd.append(i+A[i])
    
    #sort it (sort is done by first element in internal pair)
    pointsStart.sort()
    pointsEnd.sort()
    
    #number of disc pairs intersections
    count = 0
    
    #index of disc end we are working with now
    end_index = 0
    
    #index of disc start we are working with now
    start_index = 0
    
    #now we go over each end of disc
    for end_index in range(0, len(A)):
        #now we get the index of last disc whose start is before end of current disc
        while start_index < len(A) and pointsEnd[end_index] >= pointsStart[start_index]:
            start_index+=1
        #once we have found index of the first disc whose start is BEYOND end of current disc
        #we calculate how many discs are there between them (-1 since we cound disc itself)
        count += start_index - end_index - 1
        if count > 10000000:
            return -1  
    return count
