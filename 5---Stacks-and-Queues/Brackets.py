#function which checks if string S is properly nested
#given 3 types of brackets - (, [ and {
#([]) is 1
#{() is 0
#if empty - 1

def solution(S):
    #these guys are opening new level of nesting
    leftSide = {"[","(", "{"}
    
    #dictionary to show which bracket closes which one
    closes = {"]":"[", ")":"(", "}":"{"}
    
    #stack to keep the track of what is happening
    stack = []
    
    #go over each element in string
    for i in S:
        #if we open the bracket level - add it to stack
        if i in leftSide:
            stack.append(i)
        else:
            #we can't close if stack is empty
            if len(stack) == 0:
                return 0
            #if we close the wrong level of nesting - we are wrong
            if closes[i] != stack.pop():
                return 0
                
    #if some unclosed level of nesting is left - wrong!
    if len(stack) == 0:
        return 1
    else:
        return 0
