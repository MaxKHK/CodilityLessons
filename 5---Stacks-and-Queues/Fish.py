#function which calculates how much fish is left
#A - weights of fish
#B - direction (0 - left, 1 - right)
#if fish meet the one with bigger weight eats other one

def solution(A, B):
    #lets use 2 stacks
    #stack for those flowing right
    toRight = []
    
    #counter for result
    result = 0
    #go over each of the fish
    for i in range(0,len(A)):
        #goes to right, add to stack
        if B[i] == 1:
            toRight.append(A[i])
        #goes left
        else:
            #no one to intercept yet - survives for sure
            if len(toRight) == 0:
                result+=1
            #we have an interception
            else:
                #sequence of fights between competitors
                while(len(toRight)>0):
                    theCompetitor = toRight.pop()
                    #the one to right wins - add it back and get rid of the while stuff - end of story
                    #if not - it have another fight
                    if theCompetitor > A[i]:
                        toRight.append(theCompetitor)
                        break
                #while finished - what happened? Either the one to the right have won
                #and no one escapes to the left
                #or the one who goes left ate everyone - than it survives
                if len(toRight) == 0:
                    result+=1
    
    #assume that everyone to left was eaten so we have some
    #guys who go right in the end. They all survive
    result+=len(toRight)
    
    return result
