#function which counts how many rectangular
#blocks is needed to build a wall of specified size

def solution(H):
    #number of needed blocks
    count = 0
    
    #stack of heights
    stack = []
    
    #go over each height in sequence
    for i in range(0,len(H)):
        #if current block's height is less than the previous one
        #the previous block ends now (we can't build it with rectangular block)
        #so everything before is finished
        while len(stack) != 0 and H[i] < stack[-1]:
            stack.pop()
            count+=1
        
        #if stack is empty - add current new block
        #if height is bigger than current height - just add it
        if len(stack) == 0 or H[i] > stack[-1]:
            stack.append(H[i])
            
    
    #all blocks which are still in stack will need
    #separate blocks to build
    count+=len(stack)
    return count
