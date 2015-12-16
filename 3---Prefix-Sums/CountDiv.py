#function returns the number of integers within the range [A..B] that are divisible by K
def solution(A, B, K):
    #get the remainder of dividing A on K
    rem = A%K
    #if remainder is 0 - we can say that first divisible number is range is A
    if rem == 0:
        firstOne = A
    else:
        #if not we can get the first divisible number in the range by A + K - remainder
        firstOne = A + K - rem
        #if first one is bigger than B - terrminate, it is not in range
        if firstOne>B:
            return 0
    #how many numbers are there between B and first divisible
    dist = abs(B - firstOne)
    #if distance is 0 there is just one number
    if dist==0:
        return 1
    else:
        return 1 + dist//K
        
