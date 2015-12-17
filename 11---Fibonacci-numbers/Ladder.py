#one have to climb a ladder.
#At the beginning you stand on first or second rung.
#After that you could step by 1 or 2 rungs each time.
#you must make a last step so that you are on the last rung.
#You are given an arrays A and B. Each member of array A represents the length
#of a ladder. Each member of B represents some number P. For each member
#of array A you need to count number of ways to climb the ladder of length with
#A[i]. And then return result of modulo operation for 2^P
#Each member of A[i] is <= len(A)



#idea is very simple. Consider that you are climbing the ladder
#with a length of X. There are 2 options when you make a last move to 
#the end of ladder - either you are in position X-1 and climb by 1
#rung, or you are currently at position X-2 and climb by 2 rungs 
#(if you are at X-2 and climb by 1 rung you actually move to the previous case)
#That means that the number of ways to cimb ladder of len X is the sum of ways to
#get to X-1 and X-2. Which means it is a fibonacci number. For len X the
#X+1 fibonnaci number is the answer (so for 4 rungs the answer is 5).


#BUT! It gets complicated. Why? Fibos are really big numbers.
#Calculating them directly can kill our machine.
#So we need to do something to avoid counting Fibo number
#and directly get the modulo. How? We use bitwise operators for that!
#best part is that if the number in right part of modulo is a power of 2
#we can easily perform modulo with a bitwise AND operation (proof is simple
#just try to do it on a paper). Thus, we do 2 things:
#1) While counting fibo numbers we limit them via modulo with the largest B
#2) When counting modulo with B members we just do a bitwise operation

def solution(A,B):
    
    #maximum B - power of 2 we will face, minus 1. We get 111111... number which we later use in
    #bitwise AND operation
    moduloLimit = pow(2, max(B))-1
    
    #maximum number of rungs we will face
    maxA = max(A)
    
    #let's get our fibo numbers
    fiboNumbers = [0]*(maxA + 2)
    fiboNumbers[1]= 1
    for i in range(2, maxA+2):
        #notice the AND operation - which limits fibo number to
        #the part we are interested in for modulo operations count
        fiboNumbers[i] = (fiboNumbers[i-1] + fiboNumbers[i-2]) & moduloLimit
        
    #our list for results
    result = [0] * len(A)
    
    #now let's go each member and get the answer
    #Number of ways to climb a ladder is i+1 fibo number
    #Then we do a bitwise AND with a current power of 2 from B to do a modulo
    for i in range(len(A)):
        result[i] = fiboNumbers[A[i]+1] & (pow(2,B[i])-1)
    
    return result
    
    
    
