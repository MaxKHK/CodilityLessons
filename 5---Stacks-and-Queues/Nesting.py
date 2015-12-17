#function which checks if string S is properly nested
#(()) is 1
#(() is 0
#if empty - 1

def solution(A):
    #count the nesting level
    count = 0
    if len(A) > 0:
        for i in range(0,len(A)):
            if A[i] == '(':
                count+=1
            else:
                count-=1
                if count<0:
                    return 0
    if count==0:
        return 1
    else:
        return 0
