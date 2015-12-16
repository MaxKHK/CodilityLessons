#A non-empty zero-indexed array A of M integers is given.
#This array represents consecutive operations:
#if A[K] = X, such that 1 <= X <= N, then operation K is increase(X)
#if A[K] = N + 1 then operation K is max counter.

def solution(N, A):
	#matrix of counter states
	counters = [0] * N
	#maximum value of any counter so far
	maxValue = 0
	#the value used in last maxCounter command
	maxCounter = 0
	for i in A:
		if (1<=i<=N):
			#lazy write of maxcounter command
			if maxCounter > counters[i-1]:
				counters[i-1] = maxCounter
			#increase one of the counters
			counters[i-1] += 1
			if counters[i-1] > maxValue:
				#if counter became biggest one - reassign maxValue
				maxValue = counters[i-1]		
		else:
			#maxCounter command - record its value for future use
			maxCounter = maxValue
	#now lets finish with it
	#go over each element in result. If value is less than maxCounter
	#it wasn't updated after last maxCounter command
	for i in range(0,N):
		if counters[i] < maxCounter:
			counters[i] = maxCounter
	return counters
