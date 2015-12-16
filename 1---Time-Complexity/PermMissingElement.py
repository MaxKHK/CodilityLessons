#we have an array with N different elements.
#The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
#For example, N = 3, A = [1,4,2], element 3 is missing.
#The task is to find the missing element


#we just sort the original array and go through it,
#comparing if the index of current element is same as the element itself
#If not - that's our missing element.

def solution(A):
    #if array is empty - than element 1 is missing
	if len(A)>0:
		A.sort()
        #go through each element and compare it with its index
		for i in range(0,len(A)):
			if A[i] != i + 1:
				return i+1
			else:
				continue
		return A[-1] + 1
	else:
		return 1
