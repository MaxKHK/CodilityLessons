#we have an array A of integers.
#Each integer is in range [-100...100].
#val(A,S) is an abs of sum of A[i]*S[i]
#where S[i] is either -1 or 1. We are looking for such S which
#minimizes the  val(A,S). Our task is to write a function which
#returns the minimal possible val(A,S).
#For example for A = [1,5,2,-2] optimal S is [-1,1,-1,1]
#and val(A,S) = 0, so our function should return 0 for such A


#Let's rephase our task a bit. First of all, since each number can be multiplied by 1 or -1
#we can assume that we are working only with absolute values in original array. So assume
#that absA = abs(A). Now, with that in mind imagine that we split that array absA into 2 subgroups, X and Y.
#In one of them we have all the numbers multiplied by 1, in other - by -1. What would be the abs sum
#of these 2 groups? It will be sum(X) - sum(Y). And we can say that we need to minimze the difference
#between 2 such hypothaetical groups. We can say that to get this done we need to form X in such way
#so that its sum is as close to sum(absA)//2 as possible (half of sum), since the sum(Y) will be
#sum(absA) - sum(X), and the closer sum(X) to half of sum(absA) the less is the difference between the
#sum(X) and sum(Y), which is what we are trying to do. After undertanding which X has the sum closest to half of the sum
#of array absA we can calculate the minimal val(A,S) by just sum(absA) - sum(X) - sum(X).

#So how can we do what we mentioned in previous step? Notice that there are not that many different numbers
#we can see in absA - just between 0 and 100. First of all we will calculate the number of times we saw
#each number in absA. Then we start to built a dynamic programming array DP. DP[i]>=0 represents if it is possible
#to achieve the sum of i with the numbers from absA. Initially DP contains only -1 (except DP[0] = 0). Then we go over each 
#number we saw in the absA. And here is the key point.
#We pick up some number curA we saw in absA. For this number we touch each DP[i]. Now is the key point.
#We update each DP[i] so that it denotes how many curA values is left for us to use in future to achieve the
#sums after DP[i]. Note that if the previous value at DP[i] >= 0 then we can set DP[i] = count[curA]
#as no value a is needed to obtain the sum i. Otherwise we must obtain sum j − a first and
#then use a number curA to get sum i. In such a situation DP[i] = DP[i-curA] − 1.
#If tl;dr, short summary - we pick up each number, for each number we go over whole DP.
#At each such pass we get further and further to the right - each DP marked on previous pass
#as reachable is updated with the number of current numbers we have now, and each time we
#we see some DP which we can reach only with the usage of our current number is updated
#with the number of numbers we have now - 1. By the last pass we get to the biggest DP we can.

#Ok, once we fully built the DP we just go and find the first non-null DP member which will represent 
#the biggest sum closest to sum(absA)//2 we could obtain. From that val(A,S) = sum(absA) - sum(X) - sum(X).


def solution(A):
    
    #first transform our A into array of absolute numbers - since we can
    #multiply each member by 1 or -1.
    absA = [abs(item) for item in A]
    
    #let's have a full sum of absA stored
    sumAbsA = sum(absA)
    
    #now let's build a dictionary which stores each number and the number of times we see it in an array
    
    numbers = {}
    for number in absA:
        numbers[number] = numbers.get(number,0) + 1
    
    
    #now we build a DP array. If DP[i] >= 0 - that means we can achieve such sum
    #initially each member of DP is -1, except the DP[0]. We need to build such array only to half of sum
    DP = [-1] * (sumAbsA // 2 + 1)
    DP[0] = 0
    
    
    #we go over each number we saw in absA array
    for number in numbers:
        #for it we scan the whole DP
        for candidate in range(0, len(DP)):
            #now, if we can achieve the sum i with previous numbers (we marked it previously)
            #we update it with the count of how much candidate numbers is left for us to use
            if DP[candidate] >= 0:
                DP[candidate] = numbers[number]
            #maybe it is possible to reach it with the previous numbers by adding candidate to some previously reached sum?
            #Remember that we use >0 because all the DP elements for sums which could be reached with the previous numbers
            #now hold the counts of how many candidate numbers is left for us to use!
            elif candidate >= number and DP[candidate - number] > 0:
                #we use one of candidate to reach this sum
                DP[candidate] = DP[candidate - number] - 1
                
                
                
                
    #cool, we built the whole DP array. Now let's just find the biggest sum we can reach - 
    #the one which is closest to half of whole sum of absA
    for halfsum in range(len(DP)-1, -1, -1):
        if DP[halfsum] >= 0:
            #now let's calculate what is left if oneof sub arrays is multiplied by 1 and other by -1
            return sumAbsA - 2*halfsum
    
    
    #well, we shouldn't get here but let's put some default return value
    return -1
