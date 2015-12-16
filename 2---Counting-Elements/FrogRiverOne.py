#frog wants to get from position 0 to position X,
#across the river. It can jump on leaves.
#There are leaves which fall into river, and the array A
#Shows when a leaf hits a position (A[3] = 2 means
#that at moment 3 leaf fall at position 2).
#we need to calculate the earliest moment when frog can get
#across the river



#the idea is trivial. We build a map which will
#hold in which positions we already have a leaf.
#We go over each element of array and each time we see
#that a leaf landed in position which is not covered yet -
#we record that there become one less uncovered positions.
#At the moment when there are no more uncovered positions left - we exit and return

def solution(X, A):
	#matrix of if there is a leaf in position
	T = [0]*X
	#how many leafs left
	counts = X
	#go over list, mark a leaf if it is not marked yet
	#if counts reach 0 - return
	for i in range(0, len(A)):
		if T[A[i]-1] == 0:
			T[A[i]-1] = 1
			counts-=1
			if counts == 0:
				return i
		else:
			continue
	return -1
