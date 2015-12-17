#we have a table and a set of N chocolates on it
#which form a circle. We start to it chocolates
#from 0 position and eat each M chocolate after current one
#leaving wrap on the place of chocolate we eat.
#Once we face a wrap we stop eating chocs.
#We need a function that will count how many chocs we eat.
#For example having N=10 and M=4 we will eat
#chocolates 0,4,8,2,6 and than we stop => total is 5

def solution(N, M):
    #extremely simple approach - 
    #N and M 'meet' at their least common multiple
    #since if i - first choc we eat and 
    #j is the second one we eat
    #there should be i*M + k*N = j*M
    #so i is 0 and we must meet at the first position
    
    
    #algo for gcd from manual
    def gcd(a,b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)
    
    #lcm is product of numbers divided by their gcd
    
    lcm = N*M/gcd(N,M)
    return lcm / M
