#a function which returns the minimum
#possible perimeter of rectangle with
#area of N

def solution(N):
    #ok, obviously the minimum possible perimeter
    #is of a rectangle which is as close
    #to square as possible
    #so we just check each number before i*i = N
    #and get the closes one
    
    #counter
    i=1
    
    #starting the analysis with basis case
    a=1
    b = N
    
    while i*i < N:
        if N%i == 0:
            a = i
            b = N/i
        i+=1
    
    
    #special case when N is a perfect square
    if i*i == N:
        a = b = i
           
    return 2*(a+b)
