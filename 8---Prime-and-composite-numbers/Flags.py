#a function which returns the maximum number
#of flags which could be set on peaks
#a peak is like 2,3,1 or 1,2,1 or smth like it.
#if you take K flags the distance between
#peaks should be less than or equal to K
#distance is diff between indexies

def solution(A):
    #first get all the picks positions
    #then for each of them store a position of next peak
    #finally, we can take maximum of sqrt(N) flags
    #for each of possible amount of flags taken we can't set more than N/i + 1 flags
    #we go over each possible i
    #and for each of them just set the flag
    #on first peak, than on next peak with pos MORE THAN I
    
    
    #counter for number of peaks
    peaks_num = 0
    
    
    #let's mark position of peak in array
    peaks = [False]*len(A)
    for i in range(1, len(A)-1):
       if A[i-1] < A[i] and A[i] > A[i+1]:
          peaks[i] = True
          peaks_num+=1
          
    #special cases
    if peaks_num == 0:
      return 0
    if peaks_num == 1:
      return 1
          
    #using peaks array iterate array A from end to start
    #and for each cell mark when the next peak will happen
    nextPeak = [0]*len(A)
    #no next peak for last element
    nextPeak[len(A)-1] = -1
    
    
    #now we go from the end to the beginning and store the index of next peak
    for i in range(len(A) - 2, -1, -1):
       if peaks[i]:
          nextPeak[i] = i
       else:
          nextPeak[i] = nextPeak[i+1]
    
    
    #now notice - we can take sqrt(A) flags at maximum 
    #(thus we are checking for such amount of possibilities
    #now for each flag set on peak, next flag can be set on
    #>=current position + i. We can determine it fast via array next
    
    
    
    
    #greedy assumption of first flag on first peak
    i = 1
    
    #result counter
    result = 0
    
    #now check each sqrt(len(A)) possibility
    while (i-1)*i <= len(A):
       #current position index which we check
       curPos = 0
       #how many flags are already set
       numFlagsSet = 0
       #now let's process current amount of possible flags
       while curPos < len(A) and numFlagsSet < i:
          #now we determine when next flag could be set
          curPos = nextPeak[curPos]
          #no additional peaks
          if curPos == -1:
             break
          #some peak exists, we set a flag on it
          numFlagsSet += 1
          #and now next possible position can be picked
          curPos += i
       
       #if more than prior record - update
       result = max(result, numFlagsSet)
       i+=1
    
    
    return result
