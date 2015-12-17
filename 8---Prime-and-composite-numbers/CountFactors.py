#a function which counts number of factors of N

def solution(N):
    #obvious thing - all factors should be less than sqrt(N)
    #so we just check all of these numbers for being factor 
    #and report the sum
    #notice that there is always a symmetrical devisor
    
    #counter
    result = 0
    
    i=1
    
    while i*i < N:
        if N%i == 0:
            result+=2
        i+=1
        
    #special case when middle is also a divisor
    if i*i == N:
        result+=1
        
    return result
