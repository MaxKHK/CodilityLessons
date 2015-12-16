#function returns minimal positive integer
#which not occurs in a sequence
def solution(A):
    #make the list unique
	A = set(A)
    #convert it back to be a list so that we can sort it
	A = list(A)
    #sort it
	A.sort()
    #our counter
	i = 1
	for element in A:
		if element <= 0:
			continue
		else:
			if element == i:
				i+=1
			else:
				return i
	return i
