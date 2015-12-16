#function to count the pairs of passing cars
#cars are moving right (0) or left (1)
#We say that a pair of cars (P, Q), where 0 <= P < Q < N
#is passing when P is traveling to the east and Q is traveling to the west.
def solution(A):
    #number of pairs so far
    res = 0
    #matrix of sums
    sums = [A[0]]
    for i in range(1, len(A)):
        #recursively calculate the sum of all elements to the left of i
        sums.append(sums[i-1] + A[i])
    
    for i in range(0, len(A)):
        if A[i] == 0:
            res+= sums[-1] - sums[i]
            #there is a limitation on number of passning cars.
            #if we get > 1,000,000,000 we must give -1
            if res > 1000000000:
                return -1
    return res
    
